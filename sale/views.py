import json
import datetime
from math import ceil

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, F, ExpressionWrapper, Sum, Count
from django.db.models.functions import ExtractQuarter
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template.defaulttags import register

from .models import Sales
from .forms import SalesForm, SaleSelector
from .models import Lots
from customers .models import Customer


def current_year():
    return datetime.date.today().year

@login_required
def sale_list(request):
    queryset_list = Sales.objects.all().order_by('-sale_date', 'code')
    st = Sales.objects.aggregate(osszes=Count('code'))
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(code__icontains=query) | Q(vjegy__icontains=query)
        )
    paginator = Paginator(queryset_list, 10)
    page = request.GET.get('page')
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        queryset_list = paginator.page(1)
    except EmptyPage:
        queryset_list = paginator.page(paginator.num_pages)
    context = {'items': queryset_list, 'st': st}
    return render(request, 'sales_list.html', context)


@login_required
def biz_list(request, qt, ya):
    pqt = (1, 2, 3, 4)
    if qt not in pqt:
        items = ''
    else:
        items = Sales.objects.filter(sale_date__quarter=qt, sale_date__year=ya)
        ag = Sales.objects.filter(sale_date__quarter=qt, sale_date__year=ya).values().aggregate(Sum('tax'), Sum('diff'), Sum('sold'), Sum('purchase'), Sum('pay'))
    context = {'items': items, 'ag': ag, 'ya': ya, 'qt': qt}
    return render(request, 'biz_list.html', context)


@login_required
def create_sale(request, code):
    ins = get_object_or_404(Lots, code=code)
    form = SalesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.creator = request.user
        obj.sold = form.cleaned_data['sold']
        obj.purchase = form.cleaned_data['purchase']
        obj.pay = form.cleaned_data['pay']
        obj.diff = obj.sold-obj.pay
        obj.tax = ceil(obj.diff*0.2126)
        form.save()
        Lots.objects.filter(code=code).update(pay=obj.pay, purchase=obj.purchase, vjegy=obj.vjegy, status_sold=True)
        return HttpResponseRedirect(reverse('sale_list'))
    else:
        errors = form.errors
    form = SalesForm(initial={'note': '', 'purchase': ins.purchase, 'pay': ins.pay}, instance=ins)
    return render(request, 'sale_create.html', {'form': form, 'errors': errors, 'ins': ins})


@login_required
def sale_selector(request):
    form = SaleSelector(request.POST or None)
    if form.is_valid():
        selcode = form.cleaned_data['selcode']
        return HttpResponseRedirect(reverse('create_sale', kwargs={'code': selcode}))
    else:
        errors = form.errors
    form = SaleSelector()
    return render(request, 'sale_select.html', {'form': form, 'errors': errors})

def completed_quarter(dt):
    prev_quarter_map = ((4, -1), (1, 0), (2, 0), (3, 0))
    quarter, yd = prev_quarter_map[(dt.month - 1) // 3]
    return quarter

@login_required
def update_sale(request, code):
    cd = get_object_or_404(Sales, code=code)
    sold = cd.sold
    pay = cd.pay
    purchase = cd.purchase
    ins = get_object_or_404(Lots, code=code)
    form = SalesForm(request.POST or None, request.FILES or None, instance=cd)
    buid = form.initial['buyer']
    if buid:
        buyer_name = Customer.objects.values_list('name', flat=True).get(pk=buid)
    else:
        buyer_name = ""
    form = SalesForm(request.POST or None,
                    initial={'buyer': buyer_name,}, instance=cd)
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.modifier = us
        obj.sold = form.cleaned_data['sold']
        obj.purchase = form.cleaned_data['purchase']
        obj.pay = form.cleaned_data['pay']
        obj.diff = int(obj.sold) - int(obj.pay)
        obj.tax = ceil(obj.diff*0.2126)
        form.save()
        Lots.objects.filter(code=code).update(pay=obj.pay, purchase=obj.purchase, vjegy=obj.vjegy, status_sold=True)
        return HttpResponseRedirect(reverse('sale_list'))
    else:
        errors = form.errors
    form = SalesForm(request.POST or None,
                    initial={'buyer': buyer_name, 'sold': sold, 'pay': pay, 'purchase': purchase}, instance=cd)
    context = {'form': form, 'errors': errors, 'ins': ins}
    return render(request, 'sale_update.html', context)

@login_required
def delete_sale(request, code):
    instance = get_object_or_404(Sales, code=code)
    if instance:
        instance.delete()
        Lots.objects.filter(code=code).update(status_sold=False)
        return HttpResponseRedirect(reverse('sale_list'))
    else:
        return HttpResponseRedirect(reverse('sale_list'))

@login_required
def auto_complete_code(request):
    q = request.GET.get('term', '')
    # users = User.objects.filter(is_active=True)
    users = Lots.objects.filter(Q(code__icontains=q))[:10]
    users_list = []

    for u in users:
        value = '%s' % (u.code)
        u_dict = {'id': u.id, 'label': value}
        users_list.append(u_dict)
    data = json.dumps(users_list)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

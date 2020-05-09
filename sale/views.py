import json

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Sales
from .forms import SalesForm, SaleSelector
from .models import Lots
from customers .models import Customer


@login_required
def sale_list(request):
    items = Sales.objects.all()
    context = {'items': items}
    return render(request, 'sales_list.html', context)


@login_required
def create_sale(request, code):
    ins = get_object_or_404(Lots, code=code)
    form = SalesForm(request.POST or None)
    customer_name = "Józsi"
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.creator = us
        form.save()
        return HttpResponseRedirect(reverse('sale_list'))
    else:
        errors = form.errors
    # form = SalesForm(instance=ins)
    customer_name = ins.customer
    form = SalesForm(request.POST or None,
                    initial={'customer': customer_name},
                    instance=ins)
    return render(request, 'sale_create.html', {'form': form, 'errors': errors})


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
from django.forms import Field
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Max, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Lots, path_and_rename
from .forms import LotsForm
from extra.models import Extras
from artists.models import Artists
from appraisers.models import Appraisers
from customers.models import Customer
from technics.models import Technics


@login_required
def lots_list(request):
    # lots = Lots.objects.all().order_by('code')
    # context = {'items': lots}
    # return render(request, 'lots_list.html', context)

    queryset_list = Lots.objects.all().order_by('-code')
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) | Q(code__icontains=query) | Q(desc__icontains=query) | Q(
                artist__name__icontains=query) | Q(technic__name__icontains=query)
        )
    paginator = Paginator(queryset_list, 10)
    page = request.GET.get('page')
    try:
        queryset_list = paginator.page(page)
    except PageNotAnInteger:
        queryset_list = paginator.page(1)
    except EmptyPage:
        queryset_list = paginator.page(paginator.num_pages)
    context = {'items': queryset_list}
    return render(request, 'lots_list.html', context)


@login_required
def create_lot(request):
    form = LotsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.creator = request.user
        obj.purchase = form.cleaned_data['purchase']
        obj.price = form.cleaned_data['price']
        obj.pay = form.cleaned_data['pay']
        obj.start = form.cleaned_data['start']
        obj.limit = form.cleaned_data['limit']
        form.save()
        return HttpResponseRedirect(reverse('lots_list'))
    else:
        errors = form.errors
    if Lots.objects.exists():
        next_code = Lots.objects.order_by('-code')[0]
        next_code = next_code.code + 1
    else:
        next_code = 600000
    if Extras.objects.filter(owner=request.user).exists():
        extra_artist = Extras.objects.filter(owner=request.user).values_list('artist', flat=True)
        aid = extra_artist[0]
        if aid is None:
            artist_name = ""
        else:
            artist_name = Artists.objects.values_list('name', flat=True).get(pk=aid)

        extra_customer = Extras.objects.filter(owner=request.user).values_list('customer', flat=True)
        cid = extra_customer[0]
        if cid is None:
            customer_name = ""
        else:
            customer_name = Customer.objects.values_list('name', flat=True).get(pk=cid)

        extra_appraiser = Extras.objects.filter(owner=request.user).values_list('appraiser', flat=True)
        apid = extra_appraiser[0]
        if apid is None:
            appraiser_name = ""
        else:
            appraiser_name = Appraisers.objects.values_list('name', flat=True).get(pk=apid)

        extra_title = Extras.objects.filter(owner=request.user).values_list('title', flat=True)
        etitle = extra_title[0]
        if etitle is None:
            title = ""
        else:
            title = extra_title[0]

        extra_wnum = Extras.objects.filter(owner=request.user).values_list('worknumber', flat=True)
        wn = extra_wnum[0]
        if wn is None:
            worknumber = ""
        else:
            worknumber = extra_wnum[0]
    else:
        artist_name = ""
        customer_name = ""
        appraiser_name = ""
        title = ""
        worknumber = ""
    form = LotsForm(initial={'code': next_code, 'artist': artist_name, 'customer': customer_name,
                             'appraiser': appraiser_name, 'title': title, 'worknumber': worknumber})
    return render(request, 'lot_create.html', {'form': form, 'errors': errors})


@login_required
def update_lot(request, code):
    cd = get_object_or_404(Lots, code=code)
    form = LotsForm(request.POST or None, request.FILES or None, instance=cd)
    # filepath = request.FILES.get('photo', False)
    # photo = path_and_rename(cd, filepath)
    purchase = cd.purchase
    pay = cd.pay
    price = cd.price
    start = cd.start
    limit = cd.limit
    cuid = form.initial['customer']
    if cuid:
        customer_name = Customer.objects.values_list('name', flat=True).get(pk=cuid)
    else:
        customer_name = ""
    apid = form.initial['appraiser']
    if apid:
        appraiser_name = Appraisers.objects.values_list('name', flat=True).get(pk=apid)
    else:
        appraiser_name = ""
    arid = form.initial['artist']
    if arid:
        artist_name = Artists.objects.values_list('name', flat=True).get(pk=arid)
    else:
        artist_name = ""
    tecid = form.initial['technic']
    if tecid:
        technic_name = Technics.objects.values_list('name', flat=True).get(pk=tecid)
    else:
        technic_name = ""
    form = LotsForm(request.POST or None,
                    initial={'customer': customer_name, 'appraiser': appraiser_name, 'artist': artist_name,
                             'technic': technic_name},
                    instance=cd)
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.modifier = us
        obj.purchase = form.cleaned_data['purchase']
        obj.price = form.cleaned_data['price']
        obj.pay = form.cleaned_data['pay']
        obj.start = form.cleaned_data['start']
        obj.limit = form.cleaned_data['limit']
        if request.FILES:
            obj.photo = request.FILES['photo']
        form.save()
        return HttpResponseRedirect(reverse('lots_list'))
    else:
        errors = form.errors
    form = LotsForm(request.POST or None,
                    initial={'customer': customer_name, 'appraiser': appraiser_name, 'artist': artist_name,
                             'technic': technic_name, 'purchase': purchase, 'price': price, 'pay': pay, 'start': start,
                             'limit': limit},
                    instance=cd)
    context = {'form': form, 'errors': errors}
    return render(request, 'lot_update.html', context)

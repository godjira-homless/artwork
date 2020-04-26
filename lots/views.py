from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Lots
from .forms import LotsForm
from extra.models import Extras
from artists.models import Artists
from appraisers.models import Appraisers
from customers.models import Customer

@login_required
def lots_list(request):
    lots = Lots.objects.all()
    context = {'items': lots}
    return render(request, 'lots_list.html', context)


@login_required
def create_lot(request):
    form = LotsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.creator = request.user
        form.save()
        return HttpResponseRedirect(reverse('lots_list'))
    else:
        errors = form.errors
    if Lots.objects.exists():
        next_code = Lots.objects.order_by('-code')[0]
        next_code = next_code.code+1
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

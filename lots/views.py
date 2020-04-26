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
        artist_name = Artists.objects.values_list('name', flat=True).get(pk=aid)
    else:
        artist_name = ""
    form = LotsForm(initial={'code': next_code, 'artist': artist_name})
    return render(request, 'lot_create.html', {'form': form, 'errors': errors})

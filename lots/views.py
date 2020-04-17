from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Lots
from .forms import LotsForm

@login_required
def lots_list(request):
    lots = Lots.objects.all()
    context = {'items': lots}
    return render(request, 'lots_list.html', context)

@login_required
def create_lot(request):
    form = LotsForm(request.POST or None)
    current_user_added = Lots.objects.all()
    if current_user_added:
        return HttpResponseRedirect(reverse('lots_list'))
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.owner = us
        form.save()
        return HttpResponseRedirect(reverse('lots_list'))
    form = LotsForm()
    return render(request, 'lot_create.html', {'form': form})

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Max
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
    form = LotsForm(request.POST or None, request.FILES)
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.creator = us
        form.save()
        return HttpResponseRedirect(reverse('lots_list'))
    else:
        errors = form.errors
        # print(form.errors.as_data())
    if Lots.objects.exists():
        next_code = Lots.objects.order_by('-code')[0]
        next_code = next_code.code+1
    else:
        next_code = 600000
    form = LotsForm(initial={'code': next_code})
    # form = LotsForm()
    return render(request, 'lot_create.html', {'form': form, 'errors': errors})

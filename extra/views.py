from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from artists.models import Artists
# from tetelek.forms import TetelekForm
from .models import Extras
from .forms import ExtrasForm


@login_required
def extra_list(request):
    extra = Extras.objects.filter(owner=request.user)
    context = {'items': extra}
    return render(request, 'extra_list.html', context)


@login_required
def create_extra(request):
    form = ExtrasForm(request.POST or None)
    current_user_added = Extras.objects.filter(owner=request.user).exists()
    if current_user_added:
        return HttpResponseRedirect(reverse('extra_list'))
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.owner = us
        form.save()
        return HttpResponseRedirect(reverse('extra_list'))
    form = ExtrasForm()
    return render(request, 'extra_create.html', {'form': form})


@login_required
def update_extra(request, slug):
    only_the_owner = Extras.objects.filter(owner=request.user, slug=slug)
    if not only_the_owner:
        return HttpResponseRedirect(reverse('extra_list'))
    instance = get_object_or_404(Extras, slug=slug)
    fr = ExtrasForm(request.POST, instance=instance)
    aid = fr.initial['artist']
    if aid:
        artist_name = Artists.objects.values_list('name', flat=True).get(pk=aid)
    else:
        artist_name = ""
    form = ExtrasForm(request.POST or None, initial={'artist': artist_name}, instance=instance)
    if form.is_valid():
        # obj = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse('extra_list'))
    return render(request, 'extra_update.html', {'form': form})


@login_required
def delete_extra(request, slug):
    instance = get_object_or_404(Extras, slug=slug, owner=request.user)
    if instance:
        instance.delete()
        return HttpResponseRedirect(reverse('extra_list'))
    else:
        return HttpResponseRedirect(reverse('extra_list'))
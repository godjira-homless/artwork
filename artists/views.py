import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Artists
from .forms import ArtistForm


@login_required
def artists_list(request):
    # artists = Artists.objects.all().order_by('name')
    artists = Artists.objects.all().order_by('name')
    query = request.GET.get("q")
    if query:
        artists = artists.filter(
            Q(name__icontains=query) | Q(bio__icontains=query)
        )
    paginator = Paginator(artists, 20)
    page_request_var = "page"
    page_number = request.GET.get(page_request_var)
    page_obj = paginator.get_page(page_number)
    context = {'object_list': artists, 'page_obj': page_obj, 'page_request_var': page_request_var}
    return render(request, 'artists_list.html', context)


@login_required
def create_artist(request):
    form = ArtistForm(request.POST or None, request.FILES)
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.created_by = us
        form.save()
        return HttpResponseRedirect(reverse('artists_list'))
    form = ArtistForm()
    return render(request, 'create_artist.html', {'form': form})


@login_required
def update_artist(request, slug):
    id = get_object_or_404(Artists, slug=slug)
    form = ArtistForm(request.POST or None, instance=id)
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.modified_by = us
        form.save()
        return HttpResponseRedirect(reverse('artists_list'))
    return render(request, 'update_artist.html', {'form': form})


@login_required
def delete_artist(request, slug):
    obj = get_object_or_404(Artists, slug=slug)
    context = {'obj': obj}
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('artists_list'))
    return render(request, "artists_delete.html", context)

@login_required
def auto_complete(request):
    q = request.GET.get('term', '')
    # users = User.objects.filter(is_active=True)
    users = Artists.objects.filter(Q(name__icontains=q))
    users_list = []

    for u in users:
        value = '%s' % (u.name)
        u_dict = {'id': u.id, 'label': value}
        users_list.append(u_dict)
    data = json.dumps(users_list)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
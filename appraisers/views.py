import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Appraisers
from .forms import AppraiserForm


@login_required
def appraisers_list(request):
    appraisers = Appraisers.objects.all().order_by('name')
    paginator = Paginator(appraisers, 20)
    page_request_var = "page"
    page_number = request.GET.get(page_request_var)
    page_obj = paginator.get_page(page_number)
    context = {'object_list': appraisers, 'page_obj': page_obj, 'page_request_var': page_request_var}
    return render(request, 'appraisers_list.html', context)


@login_required
def create_appraiser(request):
    form = AppraiserForm(request.POST or None, request.FILES)
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.created_by = us
        form.save()
        return HttpResponseRedirect(reverse('appraisers_list'))
    form = AppraiserForm()
    return render(request, 'create_appraiser.html', {'form': form})


@login_required
def update_appraiser(request, slug):
    instance = get_object_or_404(Appraisers, slug=slug)
    form = AppraiserForm(request.POST or None, instance=instance)
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.modified_by = us
        form.save()
        return HttpResponseRedirect(reverse('appraisers_list'))
    context = {'form': form}
    return render(request, 'appraiser_update.html', context)


@login_required
def delete_appraiser(request, slug):
    obj = get_object_or_404(Appraisers, slug=slug)
    context = {'obj': obj}
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(reverse('appraisers_list'))
    return render(request, "appraisers_delete.html", context)


@login_required
def auto_complete_appraiser(request):
    q = request.GET.get('term', '')
    users = Appraisers.objects.filter(Q(name__icontains=q))
    users_list = []

    for u in users:
        value = '%s' % (u.name)
        u_dict = {'id': u.id, 'label': value}
        users_list.append(u_dict)
    data = json.dumps(users_list)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
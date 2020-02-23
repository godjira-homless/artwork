from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Appraisers
from .forms import AppraiserForm


@login_required
def appraisers_list(request):
    appraisers = Appraisers.objects.all()
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
    id = get_object_or_404(Appraisers, slug=slug)
    form = AppraiserForm(request.POST or None, instance=id)
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.modified_by = us
        form.save()
        return HttpResponseRedirect(reverse('appraisers_list'))
    context = {'form': form}
    return render(request, 'appraiser_update.html', context)


@login_required
def delete_appraiser(request):
    pass
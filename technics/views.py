import json

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from .forms import TechnicForm
from .models import Technics


@login_required
def technics_list(request):
    object_list = Technics.objects.all().order_by('-create_date')
    paginator = Paginator(object_list, 20)
    page_request_var = "page"
    page_number = request.GET.get(page_request_var)
    page_obj = paginator.get_page(page_number)

    context = {'object_list': object_list, 'page_obj': page_obj, 'page_request_var': page_request_var}
    return render(request, 'technics_list.html', context)


class SearchResultsView(ListView):
    model = Technics
    template_name = 'technics_list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context['page_request_var'] = "q=" + query + "&page"
        context['object_list'] = Technics.objects.filter(Q(name__icontains=query))
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Technics.objects.filter(
            Q(name__icontains=query)
        ).order_by('-create_date')
        return object_list


@login_required
def create_technic(request):
    if request.method == 'POST':
        form = TechnicForm(request.POST)
        if form.is_valid():
            us = request.user
            obj = form.save(commit=False)
            obj.created_by = us
            form.save()
            return HttpResponseRedirect(reverse('technics_list'))
    else:
        form = TechnicForm()
    return render(request, 'technics_create.html', {'form': form})


@login_required
def update_technic(request, slug):
    id = get_object_or_404(Technics, slug=slug)
    form = TechnicForm(request.POST or None, instance=id)
    tech = form['name'].value()
    if form.is_valid():
        us = request.user
        obj = form.save(commit=False)
        obj.modified_by = us
        form.save()
        return HttpResponseRedirect(reverse('technics_list'))
    context = {'form': form, 'technic': tech}
    return render(request, 'technics_update.html', context)


@login_required
def delete_technic(request, slug):
    id = get_object_or_404(Technics, slug=slug)
    form = Technics.objects.get(slug=slug)
    form.delete()
    return HttpResponseRedirect(reverse('technics_list'))


@login_required
def technic_complete(request):
    q = request.GET.get('term', '')
    users = Technics.objects.filter(Q(name__icontains=q))
    users_list = []

    for u in users:
        value = '%s' % (u.name)
        u_dict = {'id': u.id, 'label': value}
        users_list.append(u_dict)
    data = json.dumps(users_list)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

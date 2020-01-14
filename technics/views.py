from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView
from .forms import TechnicForm
from .models import Technics


def technics_list(request):
    obj = Technics.objects.all()
    context = {'obj': obj}
    return render(request, 'technics_list.html', context)


class SearchResultsView(ListView):
    model = Technics
    template_name = 'technics_list.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Technics.objects.filter(
            Q(name__icontains=query)
        )
        return object_list


def create_technic(request):
    if request.method == 'POST':
        form = TechnicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('technics_list'))
    else:
        form = TechnicForm()

    return render(request, 'technics_create.html', {'form': form})


def update_technic(request, slug):
    id = get_object_or_404(Technics, slug=slug)
    form = TechnicForm(request.POST or None, instance=id)
    tech = form['name'].value()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('technics_list'))

    context = {'form': form, 'technic': tech}

    return render(request, 'technics_update.html', context)
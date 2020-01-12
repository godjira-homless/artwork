from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView

from .models import Customer
from .forms import CustomerForm


def index(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'customers.html', context)


def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers_list'))
    else:
        form = CustomerForm()

    return render(request, 'customers_create.html', {'form': form})


def update_customer(request, slug):
    id = get_object_or_404(Customer, slug=slug)
    form = CustomerForm(request.POST or None, instance=id)
    customer = form['name'].value()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('customers_list'))

    context = {'form': form, 'customer': customer}

    return render(request, 'customers_update.html', context)

class SearchResultsView(ListView):
    model = Customer
    template_name = 'customers.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Customer.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query)
        )
        return object_list
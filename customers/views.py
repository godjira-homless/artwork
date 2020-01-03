from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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


def update_customer(request, id=None, template_name='form.html'):
    id = get_object_or_404(Customer, pk=id)
    form = CustomerForm(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('customers_list'))

    context = {'form': form}

    return render(request, 'customers_update.html', context)

from django.http import HttpResponseRedirect
from django.shortcuts import render
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

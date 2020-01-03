from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm

def index(request):
    #persons = Person.objects.all()
    form = CustomerForm()
    context = {'form': form}
    return render(request, 'customers.html', context)

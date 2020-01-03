from django.shortcuts import render
from .models import Customer

def index(request):
    #persons = Person.objects.all()
    context = {}
    return render(request, 'customers.html', context)

from django.shortcuts import render

def index(request):
    #persons = Person.objects.all()
    context = {}
    return render(request, 'customers.html', context)

from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password': 'd19fhewahf8'})


def eggs(request):
    return HttpResponse('Eggs are so tasty')

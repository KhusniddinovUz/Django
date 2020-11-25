from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('Hello there friend')


def eggs(request):
    return HttpResponse('Eggs are so tasty')

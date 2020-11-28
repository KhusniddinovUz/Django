from django.shortcuts import render
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklomnpqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMONPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 10))

    thepass = ''

    for x in range(length):
        thepass += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepass})

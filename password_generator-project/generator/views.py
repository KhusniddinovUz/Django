from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'password': 'd19fhewahf8'})


def password(request):
    return render(request, 'generator/password.html', {'password': 'd19fhewahf8'})

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ImageApi.as_view(), )
]

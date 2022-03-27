from django.contrib import admin
from django.urls import path
from .views import example, home

urlpatterns = [
    path('', home, name='home'),
    path('example/', example, name='examp')
]

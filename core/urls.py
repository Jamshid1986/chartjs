from cgi import test
from django.contrib import admin
from django.urls import path
from .views import example, home, Chart 

urlpatterns = [
    path('', home, name='home'),
    path('example/', example, name='examp'),
    path('ev/', Chart.as_view(), name='ev'),
    
]

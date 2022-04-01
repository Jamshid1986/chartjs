from cgi import test
from django.contrib import admin
from django.urls import path
from .views import example, home, BEV, line, Chart, wheel

urlpatterns = [
    path('', home, name='home'),
    path('example/', example, name='examp'),
    path('ev/', Chart.as_view(), name='ev'),
    path('linechartjs/', line, name='lc'),
    path('wheel/', wheel, name='wheel')
    
]

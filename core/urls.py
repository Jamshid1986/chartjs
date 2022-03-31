from cgi import test
from django.contrib import admin
from django.urls import path
from .views import example, home, Chart, BEV, Gauge, LineBEV

urlpatterns = [
    path('', home, name='home'),
    path('example/', example, name='examp'),
    path('ev/', Chart.as_view(), name='ev'),
    path('linechartjs/', LineBEV.as_view(), name='lc'),
    path('gauge/', Gauge.as_view(), name='gauge'),
    path('wheel/', BEV.as_view(), name='wheel')
    
]

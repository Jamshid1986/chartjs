from multiprocessing import context
from re import template
from xml.parsers.expat import model
from django.shortcuts import render
from .models import Post, EV, BEV
from django.views.generic import ListView


# Create your views here.

class Chart(ListView):
    model = EV
    template_name = 'ev.html'

class BEV(ListView):
    model = BEV
    template_name = 'wheel.html'

class LineBEV(ListView):
    model = BEV
    template_name = 'linechartjs.html'

def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'index.html', context)

def example(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, "examp.html", context)

class Gauge(ListView):
    model = EV
    template_name = 'gauge.html'


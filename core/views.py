from multiprocessing import context
from re import template
from django.shortcuts import render
from .models import Post, EV
from django.views.generic import ListView


# Create your views here.

class Chart(ListView):
    model = EV
    template_name = 'ev.html'

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


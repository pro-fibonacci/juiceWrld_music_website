from django.shortcuts import render
from .models import *
# Create your views here.
def blog(request):
     context = {}
     return render(request, 'pages/blog.html', context)



def contact(request):
     context = {}
     return render(request, 'pages/contact.html', context)

def submitted_contact(request):
     context = {}
     return render(request, 'pages/submitted_contact.html', context)

def elements(request):
     context = {}
     return render(request, 'pages/elements.html', context)

def events(request):
     context = {}
     return render(request, 'pages/events.html', context)

def index(request):
     home_details = home.objects.all()
     context = {"home": home_details}
     return render(request, 'pages/index.html', context)

def album_store(request):
     context = {}
     return render(request, 'pages/album_store.html', context)

def base(request):
     context = {}
     return render(request, 'pages/base.html', context)



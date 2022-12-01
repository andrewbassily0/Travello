from django.shortcuts import render
from .models import Destination
from django.conf import settings
from django.conf.urls.static import static
from news.models import News

def index(request):
    dest=Destination.objects.all()
    new=News.objects.all()
    
    return render(request, 'index.html' ,  {'dest': dest ,'new':new})


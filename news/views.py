from django.shortcuts import render
from .models import News
from news.models import News
# Create your views here.

def news(request):
    new = News.objects.all()
   
    return render(request, 'news.html', {'new': new})
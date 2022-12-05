from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate , login , logout
# Create your views here.
@csrf_exempt
def log (request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
      login (request, user)
      return render(request,'index.html')
    else:
      messages.success(request, 'Incorrect username or password')
      return redirect('log')
  else:
      return render (request , 'login.html')

def log_out(request):
  logout(request)
  messages.success(request, 'You have been logged out')
  return redirect('index')


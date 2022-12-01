from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate , login , logout
# Create your views here.
@csrf_exempt
def register (request):
   if request.method == "POST":
     username = request.POST['username']
     email = request.POST['email']
     password = request.POST['password1']
     password1 = request.POST['password2']

     user = User.objects.create_user( username , email, password )
     user.save()
     messages.success(request, 'your account was successfully created')
     return redirect('log')

   return render(request,  'register.html' )
   
@csrf_exempt
def log (request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username , password=password)
        if user is not None:
                login (request , user)
                uname = user.username 
                return render (request , 'index.html' , {'uname':uname})
        else:
                messages.error(request, 'username or password is incorrect')
                

    return render (request , 'login.html')

@csrf_exempt
def sign_out (request):
    logout(request)
    messages.success(request , 'logout Successfully')
    return redirect('index' ['logout':logout])
    
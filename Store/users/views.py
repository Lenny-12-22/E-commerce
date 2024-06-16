from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    if request.method =="POST":
        user= User.objects.filter(username = username)

        if user is not None:
            authenticate(username =username, password = password)
            login(request, user)
            return redirect('home.html')
        else:
            messages.error(request, ("an error occured try again"))
            return redirect('login')
    return render(request, 'login.html')



def register_user(request):
    

    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 !=password2:
            messages.error(request, ("password !match"))
            return render(request, 'register_user.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, ("username taken"))
            return render(request, 'register_user.html')
        
        user = User.objects.create_user(request, username=username, password=password1)
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'register_user.html')
        

    
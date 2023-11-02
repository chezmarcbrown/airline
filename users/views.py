from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    if request.user.is_authenticated:
        return render(request, 'users/index.html')
    else:
        return redirect('users:login')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', 'users:index')
            return redirect(next_url)
        else:
            return render(request, "users/login.html",
                          {"message": "Invalid credentials. Try again."})
    else:
        next_url = request.GET.get('next')
        return render(request, "users/login.html", context={'next_url': next_url})

def logout_view(request):
    logout(request)
    #return render(request, 'users/login.html', {"message": "Logged out"})
    return redirect('users:login')

from django.db import IntegrityError
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        u = request.POST["username"]
        p1 = request.POST["password"]
        p2 = request.POST["confirmation"]
        
        if p1 != p2:
            return render(request, "users/register.html", {"message": "Passwords don't match"})
        
        try:
            user = User.objects.create_user(username=u, password=p1)
            user.save()
        except IntegrityError:
            return render(request, "users/register.html", {"message": "User name taken"})
        
        login(request, user)
        return redirect('users:index')
    else:
        return render(request, 'users/register.html')
    
    
        

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import UserProfile


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        uname=request.POST['username']
        gen=request.POST['gender']
        con=request.POST['country']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        
        uname_check=User.objects.filter(username=uname).exists()
        
        if uname_check==True:
            messages.error(request,'Username is already exists')
            return redirect('signup')
        
        elif len(uname)>5:
            messages.error(request,'Username must be 5 digit')
            return redirect('signup')
            
        elif pass1!=pass2:
            messages.error(request,"Password didn't match")
            return redirect('signup')
        
        else:
            # fm=User.objects.create_user(uname,email,pass1,gen,con)
            # fm.save()
            fm=User.objects.create_user(uname,email,pass1)
            # Create a new UserProfile instance
            profile = UserProfile.objects.create(
                user=fm,
                gender=gen,
                country=con
            )
            profile.save()
            # Success Message
            messages.success(request,f'{uname} account is successfully created')
            return redirect('login')
    return render(request,'signupc.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        uname=request.POST['username']
        pass1=request.POST['password']
        user=authenticate(request,username=uname,password=pass1)
        
        if user!= None:
            auth_login(request,user)
            messages.success(request,f'{uname} Successfully Login')
            return redirect('home')                 # Main page to logout it.
        else:
            messages.error(request,'Something Went Wrong')
            return redirect('login')
    return render(request,'signinc.html')

def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('login')

def logout(request):
    auth_logout(request)
    messages.success(request,'Successfully Logout')
    return redirect('signup')

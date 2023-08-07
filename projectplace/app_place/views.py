from contextlib import redirect_stderr
from http.client import HTTPResponse
from multiprocessing import context
from pickle import NONE
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='stdlogin')
def index(request):
    return render(request, 'home.html')
@login_required(login_url='stdlogin')
def about(request):
   return render(request, 'about.html')
def contactus(request):
    return render(request, 'contact.html')
def stdRegister(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account is created for '+user)
            return redirect('stdlogin')
    
    context={'form':form}
    return render(request, 'registerS.html', context)
def stdLogin(request):
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'loginS.html', context)
    
    return render(request, 'loginS.html', context)

def logoutUser(request):
    logout(request)
    return redirect('stdlogin')


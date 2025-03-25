from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .forms import CustomerForm
from django.contrib import messages
from django.contrib.auth.models import User
from base.models import CustomerClass

"""def registration(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = CustomerForm()
    return render(request,'registration.HTML',{'form': form})"""

def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request,'password does not match ')
            return redirect('home')
        
        if CustomerClass.objects.filter(username=username).exists():
            messages.error(request,'username already taken')
            return redirect('registration')

        user = CustomerClass.objects.create_user(username=username,password=password,email=email)
        user.set_password(password)
        user.save()
        messages.success(request,'successfull')
        
    return render(request, 'registration.HTML')

def home(request):
    return HttpResponse('home')

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Correct function
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.HTML')

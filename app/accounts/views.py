from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = User.objects.create_user(clean_data['username'], clean_data['email'], clean_data['password'])
            user.last_name, user.first_name = clean_data['last_name'], clean_data['first_name']
            user.save()
            messages.success(request, 'Register successfully', 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                dj_login(request, user)
                messages.success(request, 'Logged in successfully', 'success')
                print(request)
                return redirect('home')
            else:
                messages.error(request, 'username or password is incorrect', 'error')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', context={'form': form})


def logout(request):
    dj_logout(request)
    messages.success(request, 'User logout', 'success')
    return redirect('home')

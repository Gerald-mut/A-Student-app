from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {
        "form": form
    })

    


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('EduTrack-home'))


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            admission_number = form.cleaned_data['admission_number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=admission_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('EduTrack-home')
            else:
                return render(request, "users/login.html", {
                    "form": form,
                    "message": "invalid username or password"
                })
    else:
        form = LoginForm()
    return render(request, "users/login.html", {
        "form": form
    })


    
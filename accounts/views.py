from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='/login/')

def home(request):
    user = User.objects.filter(username = request.user.username).get()
    return render(request, 'home.html',{'user':user})

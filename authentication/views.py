from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.contrib.auth.decorators import login_required
from django.conf import settings


def connexion(request):
    form = forms.LoginForm()
    message = ''
    
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides'
    return render(request, 'authentication/login.html', context={'form': form, 'message': message})

@login_required
def home(request):
    return render(request, 'blog/home.html')

def signout(request):
    logout(request)
    return redirect('login')


def inscription(request):
    form=forms.SinupForm()
    if request.method=='POST':
        form=forms.SinupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/sinup.html', context={'form': form})









from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms_account import RegistrationForm, AuthForm


def registration(request):
    """ Creating user"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'error email')
            elif password != confirm_password:
                messages.error(request, "Mots de passe différents : merci de saisir le même mot de passe.")
            else:
                user = User.objects.create(username=username, email=email, password=password)
                # bug messages.success(request, "Votre compte vient d'être créer!")
                login(request, user)
                return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'guest/signup.html', locals())


def login_view(request):
    """ log a user in"""
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = authenticate(username=username, password=password)
                if user is None:
                    # Redirect to a success page.
                    user = User.objects.get(username=username, password=password)
                    login(request, user)
                    messages.success(request, 'success')
                return redirect('index')
            except User.DoesNotExist:
                # Return an 'invalid login' error message.
                messages.error(request, 'Identifiant ou mot de passe incorrect')
    else:
        form = AuthForm()
    return render(request, 'guest/login.html', locals())


def logout_view(request):
    """log a user out -> redirect to a success page"""
    logout(request)
    return redirect('index')

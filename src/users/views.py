from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect


def login(request):
    if request.method == "POST":
        username = request.POST.get("login_username")
        password = request.POST.get("login_password")
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user and authenticated_user.is_active:
            django_login(request, authenticated_user)
            return redirect('home_page')
        else:
            messages.error(request, "Usuario incorrecto o inactivo")
    return render(request, "login_form.html")

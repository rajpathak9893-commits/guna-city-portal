# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")   # ✅ urls.py mein name="home" hona chahiye
    return render(request, "register.html", {"form": form})

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")   # ✅ same
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")          # ✅ urls.py mein name="login" hona chahiye

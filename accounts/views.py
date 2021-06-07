from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from rest_framework.decorators import api_view
# Create your views here.


def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request,user_)
        return redirect('/')
    context={'form' : form,
     "btn_label" : "Login",
     "title" : "LogIn"}
    return render(request, "accounts/auth.html", context)

def logout_view(request, *args, **kwargs):
    if request.method=='POST':
        logout(request)
        return redirect('/login')
    context={'form' : None ,
        "btn_label" : "logout",
        "title" : "Logout"}
    return render(request, "accounts/auth.html", context)


def registration_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get('password1'))
        # print(form.cleaned_data)
        # username = form.cleaned_data.get('username')
        login(request,user)
        return redirect('/login')
    context={'form' : form,
            "btn_label" : "Register",
            "title" : "Register"}
    return render(request, "accounts/auth.html", context)



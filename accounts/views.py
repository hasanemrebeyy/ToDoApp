from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
# Create your views here.
from django.template import RequestContext
from django.utils.datastructures import MultiValueDictKeyError

from accounts.forms import UserForm


def login_view(request):
    if request.user.is_authenticated():
        return redirect('todo:index')
    template_name="login.html"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('todo:index')
            else:
                return render(request, template_name, {'error_message': 'Your account has been disabled'})
        else:
            return render(request,template_name, {'error_message': 'Invalid login'})
    return render(request, template_name)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def register(request):
    return render(request, "register.html")


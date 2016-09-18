from django.shortcuts import render, redirect
# from account.models import Account
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from account.forms import UserCreateForm
from board.views import home
# Create your views here.

def account_login(request):
    auth_form = AuthenticationForm(None, request.POST or None)
    if auth_form.is_valid():
        login(request, auth_form.get_user())
        return redirect('/')

    return render(request, 'login.html', {'auth_form':auth_form})



def account_logout(request):
    logout(request)
    return redirect('/')

def account_add(request):
    if request.method =='POST':
        # form = UserCreateForm(data=request.POST or None)
        form = UserCreationForm(request.POST)
    # form = UserCreationForm()
        if form.is_valid():
            print('success')
            form.save(True)
            return redirect('login')
        else:
            print(form.errors)
            # print(form.password1.errors)
            print('Fail')
    else:
        # form = UserCreateForm()
        form = UserCreationForm()
         
    return render(request, 'add.html', {'form':form})

def account_delete(request):
    pass

def account_update(request):
    pass
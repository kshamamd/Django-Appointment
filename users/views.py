from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from .models import New


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Create your views here. give the path correctly!


def login(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('user_status')
    else:
        form = UserRegisterForm()
    return render(request, 'users/login.html')


# return redirect('new')


def logout(request):
    return render(request, 'users/logout.html')


@login_required
# provide functionality to existing function user have to login to access this page
def new(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        role = request.POST.get('role')
        number = request.POST.get('number')
        date = request.POST.get('date')
        optional_number = request.POST.get('optional_number')
        address = request.POST.get('address')
        reason = request.POST.get('reason')
        new_n = New(name=name, surname=surname, role=role, number=number, date=date,
                    optional_number=optional_number, address=address, reason=reason)
        new_n.save()
        messages.success(request, f'request send to administration !')
        # return redirect('login')
    else:
        return render(request, 'users/new.html')


def user_status(request):
    return render(request, 'users/user_status.html')
# something must be here
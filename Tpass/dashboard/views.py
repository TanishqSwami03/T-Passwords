from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from .models import *
# Create your views here.

# spaces = [
#     'Show all',
#     'Password',
#     'Secure Notes',
#     'Payments'
# ]

def dashboard_home(request):
    spaces = Space.objects.all()
    context = {'spaces':spaces}
    return render(request, 'dashboard_home.html', context)

def logout_user(request):
    logout(request)
    # messages.success(request, "You have logged out successfully !")
    return redirect('home')

def remove_items(request):
    return render(request, 'remove_items.html', {})

def add_items(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        created_updated = request.POST['created_updated']
        other_details = request.POST['other_details']

        password_item = PasswordItems(
            name = name,
            username = username,
            password = password,
            created_updated = created_updated,
            other_details = other_details,
        )
        password_item.save()

        return render(request, 'dashboard_home.html', {})
    else:
        return render(request, 'add_items.html', {})
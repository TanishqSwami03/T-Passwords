from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def dashboard_home(request):
    return render(request, 'dashboard_home.html', {})
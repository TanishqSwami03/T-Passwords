from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "You are successfully logged in !")
            return redirect('dashboard_home')
        else:
            # messages.success(request, "Error occured, try again !")
            return redirect('login_user')
    
    else:   
        return render(request, 'login.html', {})
    
def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_home')
            else:
                return redirect('signup_user')

    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})

    return render(request, 'signup.html', {'form':form})

def logout_user(request):
    logout(request)
    # messages.success(request, "You have logged out successfully !")
    return redirect('login_user')


# def dashboard(request):
#     if request.user.is_authenticated:
#         # messages.success(request, "Welcome to the T-Passwords Dashboard.")
#         return render(request, 'dashboard.html', {})
    
#     else:
#         # messages.success(request, "You have to be logged in to use the dashboard.")
#         return render(request, 'home.html', {})
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard_home(request):
    password_items = PasswordItem.objects.all()
    space = Space.objects.all()

    # search_password = request.objects.get('search_passwords')


    context = {'space':space, 'password_items':password_items}
    return render(request, 'dashboard_home.html', context)

def logout_user(request):
    logout(request)
    # messages.success(request, "You have logged out successfully !")
    return redirect('home')

def remove_items(request, item_id):
    passitem = PasswordItem.objects.get(pk=item_id)
    passitem.delete()
    return redirect('dashboard_home')

def add_items(request):
    # space = Space.objects.all()    
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # space = request.POST.get('space')
        other_details = request.POST.get('other_details')

        password_item = PasswordItem(
            name = name,
            username = username,
            password = password,
            # space = space,
            other_details = other_details,
        )
        password_item.save()
        return redirect('dashboard_home')
    return render(request, 'dashboard_home.html', {})
    # else:
    #     return render(request, 'dashboard_home.html', {'space':space})


def edit_items(request,item_id):
    item = PasswordItem.objects.get(pk=item_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        other_details = request.POST.get('other_details')
        
        item.name = name
        item.username = username
        # item.space = space
        item.password = password
        item.other_details = other_details
        item.save()
        
        return redirect('dashboard_home')
    
    context = {'item':item}
    return render(request, 'edit_items.html', context)

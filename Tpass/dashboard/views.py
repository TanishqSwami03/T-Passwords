from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.

@login_required
def dashboard_home(request):

    user = request.user

    password_items = PasswordItem.objects.filter(user = request.user)
    space = Space.objects.all()

    # search_password = request.objects.get('search_passwords')


    context = {'space':space, 'password_items':password_items}
    return render(request, 'dashboard_home.html', context)

@login_required
def logout_user(request):
    logout(request)
    # messages.success(request, "You have logged out successfully !")
    return redirect('home')

def remove_items(request, item_id):
    passitem = PasswordItem.objects.get(pk=item_id)
    passitem.delete()
    return redirect('dashboard_home')

# def add_items(request):
#     # space = Space.objects.all()    
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # space = request.POST.get('space')
#         other_details = request.POST.get('other_details')

#         password_item = PasswordItem(
#             name = name,
#             username = username,
#             password = password,
#             # space = space,
#             other_details = other_details,
#         )
#         password_item.save()
#         return redirect('dashboard_home')
#     return render(request, 'dashboard_home.html', {})
    # else:
    #     return render(request, 'dashboard_home.html', {'space':space})


def add_or_edit_item(request, item_id=None):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        other_details = request.POST.get('other_details')
        item_id = request.POST.get('item_id')  # Ensure this is correctly obtained

        if item_id:
            password_item = get_object_or_404(PasswordItem, id=item_id, user=request.user)
            password_item.name = name
            password_item.username = username
            password_item.password = password
            password_item.other_details = other_details
            password_item.save()
        else:
            PasswordItem.objects.create(
                user=request.user,
                name=name,
                username=username,
                password=password,
                other_details=other_details,
            )
        return redirect('dashboard_home')

    password_item = None
    if item_id:
        password_item = get_object_or_404(PasswordItem, id=item_id, user=request.user)

    context = {
        'item': password_item,
    }
    return render(request, 'add_items.html', context)



def edit_items(request, item_id):
    item = get_object_or_404(PasswordItem, id=item_id, user=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        other_details = request.POST.get('other_details')
        
        item.name = name
        item.username = username
        item.password = password
        item.other_details = other_details
        item.save()
        
        return redirect('dashboard_home')
    
    print(f"PasswordItem: {item}")

    context = {'item': item}
    return render(request, 'edit_items.html', context)

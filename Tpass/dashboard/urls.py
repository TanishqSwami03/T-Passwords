from django.urls import path
from . import views

urlpatterns = [
    path('dashboard_home/', views.dashboard_home, name = "dashboard_home" ),
    path('logout/', views.logout_user, name='logout_user'),
    path('remove_items/', views.remove_items, name='remove_items'),
    path('add_items/', views.add_items, name='add_items'),
    path('remove_items/<int:item_id>/', views.remove_items, name='remove_items'),
    path('edit_items/<int:item_id>/', views.edit_items, name='edit_items'),
]
from django.contrib.auth.forms import UserCreationForm
from dashboard.models import CustomUser
from django import forms

# sign-up form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ['username','name', 'email', 'password1', 'password2']
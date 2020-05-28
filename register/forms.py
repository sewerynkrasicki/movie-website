from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User

# Dziedziczymy po UserCreationForm
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        # Kolejnosc wstawiania
        fields = ["username", "email", "password1", "password2"]
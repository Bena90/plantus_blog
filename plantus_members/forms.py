from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class CustomRegisterForm (UserCreationForm):
    username    = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email       = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    last_name   = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1   = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2   = forms.CharField(
        label   ='Repita Contraseña', 
        widget  =forms.PasswordInput(attrs={'class': 'form-control'}))
        
    
    class Meta:
        model   = User
        fields  = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))
from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import PasswordChangeForm
from blog.models import Profile


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

class UserUpdateForm(forms.ModelForm):
    email       = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    last_name   = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name  = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']

class UserEditProfileForm(forms.ModelForm):
    class Meta:
        model   = Profile
        fields  = ['description', 'avatar', 'instagram_url','facebook_url']
        widgets = {
            'description'   : forms.Textarea(attrs={'class': 'form-control'}),
            'instagram_url' : forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url'  : forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProfileForm (forms.ModelForm):
    class Meta:
        model = Profile
        fields  = ['description', 'avatar', 'instagram_url','facebook_url', 'user']
        widgets = {
            'description'   : forms.Textarea(attrs={'class': 'form-control'}),
            'instagram_url' : forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url'  : forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'id':'user_id'}),

        }

class UserPasswordForm(PasswordChangeForm):
    old_password    = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    new_password1   = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password2   = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['old_password, new_password1, new_password2']


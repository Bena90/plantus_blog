from django.views.generic import CreateView, FormView
from django.contrib.auth import views as auth_views

from django.urls import reverse_lazy
from plantus_members.forms import CustomRegisterForm, LoginForm
from django.shortcuts import resolve_url

class UserRegisterView (CreateView):
    form_class  = CustomRegisterForm
    template_name    = 'registration/register.html'
    success_url = reverse_lazy ('login')

class UserLoginView (auth_views.LoginView):
    template_name   = 'registration/login.html'
    form_class      = LoginForm

    def get_success_url(self):
        return resolve_url('home')
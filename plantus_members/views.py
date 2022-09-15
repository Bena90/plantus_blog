from django.views.generic import CreateView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView


from django.urls import reverse_lazy
from plantus_members.forms import CustomRegisterForm, LoginForm, UserUpdateForm, UserPasswordForm
from django.shortcuts import resolve_url

class UserRegisterView (CreateView):
    form_class      = CustomRegisterForm
    template_name   = 'registration/register.html'
    success_url     = reverse_lazy ('login')

class UserLoginView (auth_views.LoginView):
    template_name   = 'registration/login.html'
    form_class      = LoginForm

    def get_success_url(self):
        return resolve_url('home')

class UserUpdateView (LoginRequiredMixin, UpdateView):
    model = User
    form_class      = UserUpdateForm
    template_name   = 'registration/update_profile.html'
    success_url     = reverse_lazy ('home')

    def get_object(self, queryset=None):
        return self.request.user

class UserChangePassword (PasswordChangeView):
    form_class = UserPasswordForm
    success_url = reverse_lazy('home')

    

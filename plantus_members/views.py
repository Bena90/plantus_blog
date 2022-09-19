from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404
from blog.models import Profile, Category
from django.urls import reverse_lazy
from plantus_members.forms import CustomRegisterForm, LoginForm, UserUpdateForm, UserPasswordForm, UserEditProfileForm, ProfileForm
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

class UserAddProfileView(LoginRequiredMixin, CreateView):
    model           = Profile
    form_class      = ProfileForm
    template_name   = 'user_add_profile.html'
    success_url     = reverse_lazy ('home')
    success_message = "Profile created successfully!"

class UserEditProfileView (LoginRequiredMixin, UpdateView):
    model = Profile
    form_class      = UserEditProfileForm
    template_name   = 'user_edit_profile.html'
    success_url     = reverse_lazy ('home')

class UserChangePassword (PasswordChangeView):
    form_class  = UserPasswordForm
    success_url = reverse_lazy('home')

class UserProfileView (LoginRequiredMixin, DetailView):
    model           = Profile
    template_name   = "user_details.html"

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        context['page_user'] = page_user
        return context

    

from django.urls import path
from .views import  UserRegisterView, UserLoginView, UserUpdateView, UserChangePassword

urlpatterns = [
    path('', UserRegisterView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('update_profile/', UserUpdateView.as_view(), name="update_profile"),
    path('password/', UserChangePassword.as_view(template_name='registration/change_password.html'), name="password"),
]

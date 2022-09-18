from django.urls import path
from .views import  UserRegisterView, UserLoginView, UserUpdateView, UserChangePassword, UserProfileView, UserEditProfileView

urlpatterns = [
    path('', UserRegisterView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('update_profile/', UserUpdateView.as_view(), name="update_profile"),
    path('password/', UserChangePassword.as_view(template_name='registration/change_password.html'), name="password"),
    path('user_profile/<int:pk>/', UserProfileView.as_view(template_name='user_details.html'), name="user_profile"),
    path('user_edit_profile/<int:pk>/', UserEditProfileView.as_view(), name="edit_profile"),
]

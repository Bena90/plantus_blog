from django.urls import path
from .views import  UserRegisterView, UserLoginView, UserUpdateView, UserProfileView

urlpatterns = [
    path('', UserRegisterView.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('update_profile/', UserUpdateView.as_view(), name="update_profile"),
    path('profile/', UserProfileView.as_view(), name="profile"),
]

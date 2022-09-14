from django.urls import path
from .views import  HomeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CategoryCreateView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    ## Post
    path('post/<int:pk>', PostDetailView.as_view(), name="post_details"),
    path('post_add/', PostCreateView.as_view(), name="post_add"),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name="post_update"),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name="post_delete"),
    ## Category
    path('category_add/', CategoryCreateView.as_view(), name="category_add"),
    path('category/<str:cats>/', CategoryView, name='category')
]

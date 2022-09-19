from django.urls import path
from .views import  HomeView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CategoryCreateView, CategoryView, CommentCreateView, About

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about/', About, name="about"),
    ## Post
    path('post/<int:pk>', PostDetailView.as_view(), name="post_details"),
    path('post_add/', PostCreateView.as_view(), name="post_add"),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name="post_update"),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name="post_delete"),
    ## Category
    path('category_add/', CategoryCreateView.as_view(), name="category_add"),
    path('category/<str:cats>/', CategoryView, name='category'),
    ## Comments
    path('post/<int:pk>/comment_add/', CommentCreateView.as_view(), name='comment_add'),
]

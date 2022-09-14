from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post, Category
from .forms import PostForm, PostFormUpdate, CategoryForm

## Auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(ListView):
    model           = Post
    template_name   = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu
        return context

## Post views:
class PostDetailView (DetailView):
    model           = Post
    template_name   = 'post_details.html'

class PostCreateView (LoginRequiredMixin, CreateView):
    model           = Post
    form_class      = PostForm
    template_name   = 'post_add.html'

class PostUpdateView (UpdateView):
    model           = Post
    form_class      = PostFormUpdate
    template_name   = 'post_update.html'

class PostDeleteView (LoginRequiredMixin, DeleteView):
    model           = Post
    template_name   = 'post_delete.html'
    success_url     = reverse_lazy ('home')

# Category views:
class CategoryCreateView (LoginRequiredMixin, CreateView):
    model           = Category
    form_class      = CategoryForm
    template_name   = 'category_add.html'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats.replace('-',' ').capitalize())
    print(cats)
    print(cats.replace('-',' ').capitalize())
    return render(request, 'category_posts.html', {'cats': cats.replace('-',' ').capitalize(), 'category_posts': category_posts})
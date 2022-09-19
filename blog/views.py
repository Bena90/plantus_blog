from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post, Category, Comment
from .forms import PostForm, PostFormUpdate, CategoryForm, CommentForm
from django.contrib.messages.views import SuccessMessageMixin

## Auth
##from django.contrib.auth.decorators import login_required
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

def About (request):
    return render(request, 'about.html')

## Post views:
class PostDetailView (DetailView):
    model           = Post
    template_name   = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        comments_list = Comment.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['comments_list'] = comments_list
        return context

class PostCreateView (LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model           = Post
    form_class      = PostForm
    template_name   = 'post_add.html'
    success_message = "Post created successfully!"

class PostUpdateView (SuccessMessageMixin, UpdateView):
    model           = Post
    form_class      = PostFormUpdate
    template_name   = 'post_update.html'
    success_message = "Post update successfully!"

class PostDeleteView (LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model           = Post
    template_name   = 'post_delete.html'
    success_url     = reverse_lazy ('home')
    success_message = "Post delete successfully!"
    

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

class CommentCreateView (LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments_add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
from django import forms
from .models import Post, Category, Comment

categories = Category.objects.all().values_list('name','name')

class PostForm(forms.ModelForm):
    class Meta:
        model   = Post
        fields  = ('title', 'author', 'body', 'category', 'post_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'id':'post_author'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categories, attrs={'class': 'form-control'}),
            'post_image': forms.URLInput(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model   = Category
        fields  = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class PostFormUpdate(forms.ModelForm):
    class Meta:
        model   = Post
        fields  = ('title', 'body', 'category','post_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categories, attrs={'class': 'form-control'}),
            'post_image': forms.URLInput(attrs={'class': 'form-control'})
        }

class CommentForm (forms.ModelForm):
    class Meta:
        model   = Comment
        fields  = ('body_comment','author_comment')
        widgets = {
            'body_comment': forms.Textarea(attrs={'class': 'form-control'}),
            'author_comment': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'id':'post_author'}),
        }
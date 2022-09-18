from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title       = models.CharField(max_length=255)
    author      = models.ForeignKey(User, on_delete = models.CASCADE)
    body        = RichTextField(blank = True, null = True)
    post_image  = models.URLField(max_length=250, default='https://dummyimage.com/600x400/e0e0e0/878787.png&text=img')
    post_date   = models.DateField(auto_now_add=True)
    category    = models.CharField(max_length=255)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    post            = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author_comment  = models.ForeignKey(User, on_delete = models.CASCADE)
    body_comment    = models.TextField()
    date_comment    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

class Profile (models.Model):
    user            = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    description     = models.TextField()
    avatar          = models.ImageField(upload_to='avatars', null=True, blank=True)
    instagram_url   = models.CharField(max_length=256,null=True, blank=True)
    facebook_url    = models.CharField(max_length=256,null=True, blank=True)

    def __str__(self):
        return str(self.user)

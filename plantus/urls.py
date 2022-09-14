from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('members/', include('plantus_members.urls')),
    path('members/', include('django.contrib.auth.urls')),
]
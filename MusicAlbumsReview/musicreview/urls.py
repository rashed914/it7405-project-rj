from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include all album-related pages
    path('', include('albums.urls')),
]

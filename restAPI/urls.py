from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('blogApiApp.urls')),
    path('movie/', include('movieApiApp.urls')),
    
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get/', views.getAllPosts),
    path('detail/<int:id>', views.getDetailPost),
    path('create/', views.createPost),
    path('delete/<int:id>', views.deletePost),
    path('update/<int:id>', views.updatePost),
]

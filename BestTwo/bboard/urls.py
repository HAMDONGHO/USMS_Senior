from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<int:post_id>/', views.detail, name="detail"),
    path('post/new/', views.post_new, name = 'new'),
    path('post/<int:post_id>/edit/', views.post_edit, name = 'edit'),
    path('post/<int:post_id>/delete/', views.post_delete, name = 'delete'),
    path('post/<int:post_id>/comment_new/', views.comment_new, name='comment_new'),
    path('post/<int:post_id>/comment_delete/', views.comment_delete, name='comment_delete'),
]
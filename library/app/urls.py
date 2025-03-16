from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('register/', views.register, name='register'),
    path('', views.login, name='user_login'),
    path('logout/', views.logout, name='user_logout'),
    path('book_list', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('update/<int:book_id>/', views.book_update, name='book_update'),
    path('delete/<int:book_id>/', views.book_delete, name='book_delete'),
    ]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
        path('', views.book_list, name='book-list'),
    path('add-book/',    views.book_form, name='book-form'),
]
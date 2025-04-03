from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.item_list, name='item-list'),

]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/new/', views.contact_create, name='contact_create'),
    path('contact/<pk>/edit/', views.contact_update, name='contact_update'),
    path('contact/<pk>/delete/', views.contact_delete, name='contact_delete'),
    path('contact/<pk>/call/', views.call_contact, name='call_contact'),
]

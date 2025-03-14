from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
     path('', home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('instructor_dashboard/', views.instructor_dashboard, name='instructor_dashboard'),
    path('submit/<assignment_id>/', views.submit_assignment, name='submit_assignment'),
     path("instructor_dashboard/", views.instructor_dashboard, name="instructor_dashboard"),
    path("add_assignment/", views.add_assignment, name="add_assignment"),
    path("edit_assignment/<int:assignment_id>/", views.edit_assignment, name="edit_assignment"),
    path("delete_assignment/<int:assignment_id>/", views.delete_assignment, name="delete_assignment"),
    path("grade_submission/<int:submission_id>/", views.grade_submission, name="grade_submission"),
]
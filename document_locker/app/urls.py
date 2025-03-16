from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('upload/', upload_document, name='upload_document'),
    path('dashboard/', list_documents, name='dashboard'),
    path('delete/<document_id>/', delete_document, name='delete_document'),
    path('edit/<document_id>/', edit_document, name='edit_document'),

]

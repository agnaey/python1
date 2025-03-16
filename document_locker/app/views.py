from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Document
import os

# Create your views here.


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username and email and password:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html')
            if User.objects.filter(email=email).exists():
                return render(request, 'register.html')
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def upload_document(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        title = request.POST.get('title', 'Untitled')
        Document.objects.create(user=request.user, title=title, file=file)
        return redirect('dashboard')
    return render(request, 'upload.html')

@login_required
def list_documents(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'documents': documents})

@login_required
def delete_document(request, document_id):
    try:
        document = Document.objects.get(id=document_id, user=request.user)
        file_path = document.file.path
        document.delete()
        if os.path.exists(file_path):
            os.remove(file_path)
    except Document.DoesNotExist:
        pass
    return redirect('dashboard')

@login_required
def edit_document(request, document_id):
    document = Document.objects.get( id=document_id, user=request.user)
    if request.method == 'POST':
        document.title = request.POST.get('title')
        if request.FILES.get('file'):
            if os.path.exists(document.file.path):
                os.remove(document.file.path)
            document.file = request.FILES['file']
        document.save()
        return redirect('dashboard')
    return render(request, 'edit.html', {'document': document})
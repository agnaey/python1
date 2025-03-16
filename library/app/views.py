from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': "Username already exists"})
        User.objects.create_user(username=username, password=password)
        return redirect('user_login')
    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  
            return redirect('book_list')
        return render(request, 'login.html', {'error': "Invalid credentials"})
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('user_login')


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@login_required
def book_create(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            published_date=request.POST['published_date'],
            quantity=request.POST['quantity']
        )
        return redirect('book_list')
    return render(request, 'book_form.html')

@login_required
def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.isbn = request.POST['isbn']
        book.quantity = request.POST['quantity']
        book.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'book': book})

@login_required
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

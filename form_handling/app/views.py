from django.shortcuts import render,redirect
from .models import *

# Create your views here.


def book_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        
        if title and author and published_date:
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('book-list')
    
    return render(request, 'book_form.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})
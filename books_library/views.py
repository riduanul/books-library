from django.shortcuts import render
from books.models import Book, Category
from django.views.generic import DetailView
# Create your views here.

def home(request, book_slug=None):
    books = Book.objects.all()
    categories = Category.objects.all()

    if book_slug is not None:
        category = Category.objects.get(slug=book_slug)
        books = Book.objects.filter(category=category)

    return render(request, 'home.html', {'books': books, 'categories': categories})



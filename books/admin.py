from django.contrib import admin
from books.models import Category, Book, Borrow, Reviews
# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Reviews)
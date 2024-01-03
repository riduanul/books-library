from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique= True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.category_name}'
    

class Book(models.Model):
    book_title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name = 'category', on_delete = models.CASCADE)
    price = models.IntegerField()
    description= models.TextField()
    image = models.ImageField(upload_to='books/media/', blank= True, null=True)
    quantity= models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.book_title}'

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,)
    borrow_date = models.DateField(auto_now_add = True)
    quantity= models.PositiveIntegerField(default=0)
    is_borrow= models.BooleanField(default=False)
    

class Reviews(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', null=True)
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add = True)
    review = models.TextField()
    
    def __str__(self):
        return f'{self.name}'
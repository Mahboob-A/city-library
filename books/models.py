from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings

from .constants import BOOK_GENRE_CATEGORY

# Create your models here.

class BookGenre(models.Model): 
        name = models.CharField(max_length=30, choices=BOOK_GENRE_CATEGORY, unique=True)
        description = models.TextField(null=True, blank=True)

        def __str__(self): 
                return self.name 
        
        
class Book(models.Model): 
        genre = models.ForeignKey(BookGenre, related_name='books', on_delete=models.CASCADE)
        isbn = models.CharField(max_length=15)
        title = models.CharField(max_length=150)
        author = models.CharField(max_length=50)
        book_image_url = models.URLField()
        description = models.TextField()
        total_copy = models.IntegerField(default=0)
        first_pub = models.DateField(auto_now_add=True)
        last_pub = models.DateField(auto_now=True, null=True, blank=True)
        
        def __str__(self): 
                return f"Name : {self.title} Author : {self.author}" 



class BorrowBook(models.Model):
        user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users', on_delete=models.CASCADE)  # relaton with custom user 
        book = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE)
        borrow_date = models.DateTimeField(auto_now=True)
        provisional_return_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=15))

        def __str__(self):
                return f"{self.user.first_name} borrowed {self.book.title}"

class ReturnBook(models.Model):
        borrow = models.ForeignKey(BorrowBook, related_name='borrow_book', on_delete=models.CASCADE)
        return_date = models.DateTimeField(auto_now=True)
        is_fine_paid = models.BooleanField(default=False)

        def __str__(self):
                return f"{self.borrow.user.username} returned {self.borrow.book.title}"
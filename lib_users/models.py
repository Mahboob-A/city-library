
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


from books.models import Book, BorrowBook



# custom user 
class User(AbstractUser):
        wishlist = models.ManyToManyField(Book, related_name='user_wishlists',  blank=True, )
        borrowed_books = models.ManyToManyField(Book, related_name='user_borrowed_books', through=BorrowBook)
        total_borrowed_books = models.IntegerField(default=0)
        












class DemoModel(models.Model): 
        name = models.CharField(max_length=30)
        email = models.EmailField()
        password = models.CharField(max_length=30)




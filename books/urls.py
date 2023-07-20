
from django.urls import path

from .views import * 

urlpatterns = [
        
        # book 
        path('book-list/', book_list, name='book_list'),
        path('borrowed-books/', user_borrowed_books, name='all_borrowed_books'),
        path('book-details/<int:book_id>/', book_detail, name='book_detail'),
        
]

from django.urls import path 

from .views import *
urlpatterns = [
        
        # book request from all books 
        path('book-request/<int:book_id>/', book_request_book_list, name='book_request_book_list'),
        
        # book request from book form 
        path('book-request/form/', book_request_form, name='book_request_form'),
        
        # book search 
        path('seach-books/', search_books, name='search_books'),
        
        # borrow book 
        path('borrow-book/<int:book_id>/', borrow_book, name='borrow_book'),
        
        # return book 
        path('return-book/<int:book_id>/', return_book, name='return_book'),
        
        # check due date 
        path('check-book-return-due-date/<int:book_id>/', check_book_return_date, name='check_book_return_date'),
        
        # pay fine 
        path('pay-overdue-fine/', pay_overdue_fine, name='pay_overdue_fine'),
]

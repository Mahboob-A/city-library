
from django.contrib import admin

from .models import  Book, BookGenre, BorrowBook, ReturnBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin): 
        list_display = ['id', 'isbn', 'title', 'author', 'total_copy', 'book_image_url', 'description', 'first_pub', 'last_pub', ]


@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'description']
        

@admin.register(BorrowBook)
class BorrowBookAdmin(admin.ModelAdmin): 
        list_display = ['id', 'user', 'book', 'borrow_date', 'provisional_return_date']
        

@admin.register(ReturnBook)
class ReturnBookAdmin(admin.ModelAdmin): 
        list_display = ['id', 'get_return_book',  'is_fine_paid', 'return_date', ]
        
        def get_return_book(self, obj): 
                return f'{obj.borrow.user.get_full_name()} returned {obj.borrow.book.title} book'
        
        get_return_book.short_description = 'Book Returned'

from django.contrib import admin

# Register your models here.
from .models import BookRequest

@admin.register(BookRequest)
class BookRequestAdmin(admin.ModelAdmin): 
        list_display = ['id', 'title', 'author', 'original_book_id', 'user_id', 'has_book_added_in_library', 'is_form_request', 'request_date', 'description']
        
        

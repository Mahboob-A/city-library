from django.contrib import admin

# Register your models here.
from .models import DemoModel, User
@admin.register(User)
class UserAdmin(admin.ModelAdmin): 
        list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'total_borrowed_books', 'display_borrowed_books', 'display_wishlist',]
        
        def display_borrowed_books(self, obj): 
                all_borrowed_books = obj.borrowed_books.all()
                return ', '.join([book.title for book in all_borrowed_books])

        display_borrowed_books.short_description = 'Borrowed Books'
        
        def display_wishlist(self, obj): 
                all_wishlist = obj.wishlist.all()
                return ', '.join([book.title for book in all_wishlist])

        display_wishlist.short_description = 'Wishlisted Books'
        

                

        

        


# @admin.register(Wishlist)
# class WishlistAdmin(admin.ModelAdmin):
#         list_display = ['id', 'name', 'created_at']

# @admin.register(DemoModel)
# class DemoModelAdmin(admin.ModelAdmin): 
#         list_display = ['id', 'name', 'email', 'password']
        
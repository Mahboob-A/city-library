from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Book, BookGenre, BorrowBook, ReturnBook

# Create your views here.

# templates are in the templates/lib_users


@login_required(login_url='login')  # Redirect to 'login' if the user is not authenticated
def book_list(request):
        books = Book.objects.all()
        genres = BookGenre.objects.all()
        context = {
                'books': books,
                'genres': genres,
        }
        return render(request, 'lib_users/book_list.html', context)




@login_required(login_url='login')
def user_borrowed_books(request): 
        '''
        Shows all the borrowed books of the user 
        '''
        template_path = 'lib_users/borrow_or_wishlist.html'
        user = request.user
        all_borrowed_books = user.borrowed_books.all()
        
        if all_borrowed_books.exists(): 
                return render(request, template_path, {'all_borrowed_books' : all_borrowed_books})
        else: 
                return render(request, template_path, {'no_borrowed_books' : True})
        


@login_required(login_url='login')
def book_detail(request, book_id): 
        ''' 
        shows a single book details using book id 
        '''
        template_path = 'lib_users/book_detail.html'
        
        # To show custom message that this book is wishlisted 
        book_wishlist = False 
        if request.session['book_wishlist']: 
                book_wishlist = True 
                del request.session['book_wishlist']
        
        book = Book.objects.get(pk=book_id)
        return render(request, template_path, {'book' : book, 'book_wishlist' : book_wishlist})


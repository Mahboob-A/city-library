
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
from books.models import Book


@login_required(login_url='login')
def make_wishlist(request, book_id): 
        '''
        Makes a book into Users wishlist using book id 
        '''
        template_path = 'lib_users/show_errors.html'
        book = get_object_or_404(Book, id=book_id)
        user = request.user
        
        if user.borrowed_books.filter(id=book_id).exists(): 
                return render(request, template_path, {'book_title' : book.title, 'book_exists_borrowed_trying_wishlist' : True})
        
        if user.wishlist.filter(id=book_id).exists(): 
                return render(request, template_path, {'book_title' : book.title,  'book_exists_already_wishlisted' : True})


        user.wishlist.add(book)
        user.save()
        request.session['book_wishlist'] = True  # see book detail func in books 
        return redirect('book_detail', book_id=book_id)




@login_required(login_url='login')
def remove_from_wishlist(request, book_id): 
        book = get_object_or_404(Book, id=book_id)
        user = request.user 
        user.wishlist.remove(book)
        return redirect('wishlist')

@login_required(login_url='login')
def user_wishlist(request): 
        '''
        Shows all the wishlist books of the user 
        '''
        template_path = 'lib_users/borrow_or_wishlist.html'
        user = request.user
        wishlist = user.wishlist.all()
        return render(request, template_path, {'wishlist' : wishlist})
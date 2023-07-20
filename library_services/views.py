from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils import timezone
from datetime import date


from .models import BookRequest
from wallet.models import Wallet
from books.models import Book, BorrowBook, ReturnBook, BookGenre
from .forms import BookRequestModelForm, PayFineForm

@login_required(login_url='login')
def book_request_book_list(request, book_id):
        '''
        Receiving book request form the Book List. Here only saving the book id and the user id 
        is_form_request is False 
        '''
        template_path = 'library_services/book_request_message.html'
        book = Book.objects.get(id=book_id)  # to show the book name in template 
        user = request.user 
        if BookRequest.objects.filter(original_book_id=book_id, user_id=user.id).exists(): 
                return render(request, template_path, {'book_request_book_list_failed' : True, 'book_title' : book.title})
        
        # the book is not in the db so save the request 
        book_request = BookRequest(original_book_id=book_id, user_id=user.id)
        book_request.save()
        return render(request, template_path, {'book_request_book_list_success' : True, 'book_title' : book.title})
        
        

@login_required(login_url='login')
def book_request_form(request): 
        '''
        Book request from the form 
        '''
        template_path_message = 'library_services/book_request_message.html'
        template_path_form = 'library_services/book_request_form.html'
        
        if request.method == 'POST': 
                form = BookRequestModelForm(request.POST)
                if form.is_valid(): 
                        book_title = form.cleaned_data['title']
                        description = ''
                        if form.cleaned_data['description'] :
                                description = form.cleaned_data['description']
                                
                        user = request.user 
                        # if book title and user same indicates the book request is already placed by the user 
                        if BookRequest.objects.filter(title__exact=book_title, user_id=user.id).exists():
                                return render(request, template_path_message, {'book_request_form_failed' : True, 'book_title' : book_title})
                        book_request = form.save(commit=False)
                        book_request.user_id = user.id 
                        book_request.is_form_request = True
                        if description != '' : 
                                book_request.description = description 
                        book_request.save()                        
                        return render(request, template_path_message, {'book_request_form_success' : True, 'book_title' : book_title})
        else: 
                form = BookRequestModelForm()
                return render(request, template_path_form, {'form' : form})
                

@login_required(login_url='login')
def search_books(request):
        '''
        for searching books 
        '''
        
        template_path = 'library_services/search_book_result.html'
        query = request.GET.get('search')  

        if query:
                books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        else:
                books = Book.objects.all()

        return render(request, template_path,  {'books': books, 'query': query})


@login_required(login_url='login')
def check_book_return_date(request, book_id): 
        
        template_path = 'library_services/check_book_return_date.html'
        
        user = request.user 
        borrowed_book = get_object_or_404(BorrowBook, book__id=book_id, user=user)  
        book_title = borrowed_book.book.title 

        current_date = timezone.now()
        provisional_return_date = borrowed_book.provisional_return_date

        on_time = True 
        # current date is within provisional return date 
        if provisional_return_date > current_date: 
                remaining_days = (provisional_return_date - current_date).days
        else: 
                # current date exceeded the provisional return date 
                remaining_days = (current_date - provisional_return_date).days     
                on_time = False
                   
        context = {
                'on_time' : on_time, 
                'book_title' : book_title, 
                'remaining_days' : remaining_days,
                'current_date' : current_date.date(),
                'provisional_return_date' : provisional_return_date.date()
        }
        return render(request, template_path, context)

        

@login_required(login_url='login')
def borrow_book(request, book_id):
        '''
        borrowes a book. if the book already borrowed, prevents a new borrow from same user.
        
        '''
        
        template_path_error = 'lib_users/show_errors.html'
        template_path_success =  'lib_users/book_detail.html'
        
        book = get_object_or_404(Book, id=book_id)
        user = request.user
        
        if user.borrowed_books.filter(id=book_id).exists(): 
                return render(request, template_path_error, {'book_title' : book.title,  'book_exists_borrowed' : True})

        if user.total_borrowed_books > 5: 
                return render(request, template_path_error, {'book_title' : book.title, 'total_book_borrowing_limit' : 5,  'total_borrowed_books_exceeded' : True})

        if book.total_copy >= 1:
                book.total_copy -= 1  # decrease total book copy 
                book.save()
                
                # add in the manytomany field of user (relation with Book)
                user.borrowed_books.add(book)
                user.total_borrowed_books += 1 
                user.save()

                # borrowed_book = Book.objects.get(pk=book_id)
                return render(request, template_path_success, {'book' : book, 'book_borrow_successful' : True})
        else:
                # this is handled in the iterate_books.html showing unavailable (if book.total_copy) no need to handle here 
               pass 



@login_required(login_url='login')
def return_book(request, book_id): 
        
        template_path = 'library_services/book_return_result.html'
        user = request.user 
        # as the relation is foreign key , accessing the related object's field using the double underscore 
        borrowed_book = get_object_or_404(BorrowBook, book__id=book_id, user=user)  
        book_title = borrowed_book.book.title 


        current_date = timezone.now()
        borrow_date = borrowed_book.borrow_date 
        provisional_return_date = borrowed_book.provisional_return_date
        
        return_book, _ = ReturnBook.objects.get_or_create(borrow=borrowed_book)   
        is_fine_paid = return_book.is_fine_paid 
        
        # for checking purpose :  change the condition to : ( provisional_return_date.date()  <= current_date.date() ) :      in this case, make abs in the overdue_days and fine_amount in else part 
        # this will make the date is overdue for all cases 
        # and this check : (current_date.date() <= provisional_return_date.date() ):   will check the correct logic 
        if is_fine_paid or (current_date.date() <= provisional_return_date.date() ):  
                return_book.return_date = current_date
                borrowed_book.book.total_copy += 1 # assessing the Book model 
                user.total_borrowed_books -= 1  # decrease the total no of borrowed books
                user.save()  # saving the user model 
                borrowed_book.book.save()  # saving the book 
                borrowed_book.save()  # borrow book model 
                return_book.save()  # return book model 
                borrowed_book.delete()  # delete the borrow book instance form the users borrowed_books (foreign key)

                return render(request, template_path, {'book_title' : book_title,  'is_book_return_success' : True})
        
        else:   # else will trigger pay_overdue_fine view below from the template 
                fine_amount = 0 
                overdue_days = (current_date.date() - provisional_return_date.date()).days
                fine_amount = overdue_days * 5 # (5 as 5 rupees per day)
                
                # if fine_amount is 150 which is overdue_days = 25, then make the fine_amount capped at 125 
                if fine_amount > 125: 
                        fine_amount = 125
                        
                # no fine is imposed form overdue day 25 till overdue day 30 to allow the user returd the book. If overdue day > 30, 
                # then make per day overdue day charge to 7 as penalty to the user 
                if overdue_days > 30: 
                        fine_amount = overdue_days * 7 
                        
                # Access these in the pay_fine view 
                request.session['fine_amount'] = fine_amount
                request.session['return_book_id'] = return_book.id 
                
                return render(request, template_path, {'overdue_days' : overdue_days, 'fine_amount' : fine_amount,   'is_book_return_failed' : True})
        

@login_required(login_url='login')
def pay_overdue_fine(request): 
        '''
        This view is responsible for paying the fine for overdue book return 
        '''
        template_path_pay_fine = 'library_services/pay_fine_result.html'
        
        if request.session['return_book_id']: 
                return_book_id = request.session['return_book_id']
                fine_amount =  request.session['fine_amount']
                
                return_book = ReturnBook.objects.get(id=return_book_id)
                
                # accessing in this sequence : BookReturn -> BorrowBook -> Book -> title 
                book_title = return_book.borrow.book.title
                
                user = request.user 
                user_wallet, _  = Wallet.objects.get_or_create(user=user)
                user_wallet_balance = user_wallet.balance
                
                context = {'fine_amount' : fine_amount, 'user_wallet_balance' : user_wallet_balance, 'required_balance' : fine_amount - user_wallet_balance,  'fine_payment_unsuccessful' : True}
                if user_wallet_balance < fine_amount: 
                        return render(request, template_path_pay_fine, context)  
                
                initial = {'amount' : fine_amount, 'fine_amount' : fine_amount, 'wallet_balance' : user_wallet_balance}
                if request.method == 'POST': 
                        form = PayFineForm(request.POST, initial=initial)
                        if form.is_valid(): 
                                # just taking the input form the user just to show user is giving input. 
                                # we can just apply the logic below directly without any form 
                                user_wallet.balance -= fine_amount
                                return_book.is_fine_paid = True
                                return_book.save()
                                user_wallet.save()
                                return render(request, template_path_pay_fine, {'fine_amount' : fine_amount, 'book_title' : book_title,  'fine_payment_successful' : True})
                                # del  request.session['fine_amount']    # no neeed to delete the keys as in the return book view, this will be overridden each time 
                                # del request.session['return_book_id']   # but if the keys are deleted here, then any back button click would yield key eroor of return_book_id
                else: 
                        form = PayFineForm(initial=initial)
                return render(request, 'library_services/pay_fine_form.html', {'form' : form, 'fine_amount' : fine_amount, 'curr_balance' : user_wallet_balance})


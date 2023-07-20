from django.db import models

# Create your models here.



class BookRequest(models.Model): 
        '''
        if the book request from form, then get title and author from the form and make is_form_request = True to identify it is from form 
        and if request from Book List, add the book id and user id to track the user. 
        Two view will handle to operations 
        '''
        title = models.CharField(max_length=150, null=True, blank=True)
        author = models.CharField(max_length=50, null=True, blank=True)
        original_book_id = models.IntegerField(null=True, blank=True)
        user_id = models.IntegerField(null=True, blank=True)
        has_book_added_in_library = models.BooleanField(default=False)
        is_form_request = models.BooleanField(default=False)
        request_date = models.DateField(auto_now_add=True)
        description = models.TextField(max_length=250, null=True, blank=True)
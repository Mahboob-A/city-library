

from django.urls import path

from .views import * 

urlpatterns = [
        
        # all list of wishlist of the user 
        path('wishlist-list/', user_wishlist, name='wishlist'),
        
        # create a wishlist from all books
        path('make-wishlist/<int:book_id>/', make_wishlist, name='make_wishlist'),
        
        # remove book form wishlist 
        path('remove-form-wishlist/<int:book_id>/', remove_from_wishlist, name='remove_from_wishlist'),
        
        
]



from django.urls import path 
from .views import add_money

urlpatterns = [
        path('wallet/', add_money, name='wallet'),
]

"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

'''
Module 18 - Library Management Project Assignment.
Mod date : 180623
Mod begin date : 05023, Wednesday, 07.00 am 
"""

from django.contrib import admin
from django.urls import path, include

'''
most of the templats are in the templates/lib_users and templates/library_services 

templates/lib_users has all the templates of wishlist ans books app.  
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('auth/', include('lib_users.urls')),
    path('services/', include('library_services.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('books/', include('books.urls')),
    path('wallet/', include('wallet.urls')),
    
]

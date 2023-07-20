from django.contrib import admin

# Register your models here.
from .models import Wallet

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin): 
        list_display = ['id', 'user', 'get_user_full_name', 'balance']
        
        def get_user_full_name(self, obj):
                return obj.user.get_full_name()
        
        get_user_full_name.short_description = 'User Full Name'
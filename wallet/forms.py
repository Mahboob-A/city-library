
from django import forms
from django.core.validators import MinValueValidator
from .models import Wallet

class AddMoneyModelForm(forms.ModelForm): 
        balance = forms.IntegerField(
                label='Add Money',
                validators=[MinValueValidator(100, 'Minimum Add Money Is Rs. 100')],
                widget=forms.NumberInput(attrs={'class'  : 'add_balance', 'placeholder' : 'Add Money'})
        )
        class Meta: 
                model = Wallet
                fields = ['balance']
                
                # labels = {
                #         'balance' : 'Add Balance',
                # }
                
                # widgets = {
                #         'balance' : forms.NumberInput(attrs={'class'  : 'add_balance', 'placeholder' : 'Input Amount'}),

                # }
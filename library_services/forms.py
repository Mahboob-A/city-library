
from django import forms
from .models import BookRequest


class BookRequestModelForm(forms.ModelForm): 
        
        # as the title and author is nul and blank , so making these required for the form 
        def __init__(self, *args, **kwargs): 
                super().__init__(*args, **kwargs)
                self.fields['title'].required = True
                self.fields['author'].required = True  
                
        class Meta: 
                model = BookRequest
                fields = ['title', 'author', 'description']
                
                labels = {
                        'title' : 'Book Name',
                        'author' : 'Author Name',
                        'description' : 'Book Description',
                }

                error_messages = {
                        'title' : {'required' : 'Enter Book Name'},
                        'author' : {'required' : 'Enter Author Name'},
                }
                
                widgets = {
                        'title' : forms.TextInput(attrs={'placeholder' : 'Enter Book Name'}),
                        'author' : forms.TextInput(attrs={'placeholder' : 'Enter Author Name'}),
                        'description' : forms.TextInput(attrs={'placeholder' : 'Enter Some Description (You can leave it blank)'}),
                }
                

class PayFineForm(forms.Form): 
        amount = forms.IntegerField(label='Amount', widget=forms.NumberInput(attrs={'placeholder' : 'Input Amount'}))

        
        def clean_amount(self): 
                amount = self.cleaned_data['amount']
                fine_amount = self.initial['fine_amount']
                wallet_balance = self.initial['wallet_balance']
                print('amoutn form initial ', amount)
                print('fine form initial : ', fine_amount)
                print('wallet form initial : ', wallet_balance)
                
                if amount < fine_amount: 
                        raise forms.ValidationError(f'Amount Must Be Equal To Rs. {fine_amount}')
                        
                if amount > wallet_balance: 
                        raise forms.ValidationError(f'Amount Must Be Less Than Rs. {wallet_balance}')
                

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Wallet
from .forms import AddMoneyModelForm


@login_required(login_url='login')
def add_money(request): 
        '''
        adds money to the user wallet 
        '''
        template_path = 'wallet/wallet_money.html'
        
        curr_wallet, _ = Wallet.objects.get_or_create(user=request.user)
        curr_balance = curr_wallet.balance

        if request.method == 'POST': 
                form = AddMoneyModelForm(request.POST)
                if form.is_valid(): 
                        balance = form.cleaned_data['balance']
                        # print(balance)
                        curr_wallet.balance += balance
                        curr_wallet.save()
                        curr_balance = curr_wallet.balance
                        return redirect('wallet')
        else: 
                form = AddMoneyModelForm()
        return render(request, template_path, {'form' : form, 'curr_balance' : curr_balance})
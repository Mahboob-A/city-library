from django.shortcuts import render, redirect, HttpResponse
from .froms import DemoModelForm, CustomUserCreationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.




##################### BOOK RELATED FUNCTION ##########################


##################### AUTH FUNCTIONS ################################

def user_login_2(request): 
        template_path = 'lib_users/user_login.html'
        if request.method == 'POST': 
                form = DemoModelForm(data=request.POST)
                if form.is_valid(): 
                        name = form.cleaned_data['name']
                        email = form.cleaned_data['email']
                        password = form.cleaned_data['password']
                        form.save()
                        print(name, " ", email, " ", password)
                        return redirect('login')
                        
        else : 
                form = DemoModelForm()
        return render(request, template_path, {'form' : form})


def user_login(request): 
        if not request.user.is_authenticated: 
                tempalte_path = 'lib_users/user_login.html'
                if request.method == 'POST': 
                        form = UserLoginForm(request, data=request.POST)
                        if form.is_valid(): 
                                username = form.cleaned_data['username']
                                password = form.cleaned_data['password']
                                user = authenticate(username=username, password=password)
                                if user is not None: 
                                        login(request, user)
                                        return redirect('dashboard')
                        else: 
                                return render(request, tempalte_path, {'form' : form, 'error' : 'Invalid username or password'})
                else : 
                        form = UserLoginForm()
                        return render(request, tempalte_path, {'form' : form})
        else: 
                return redirect('dashboard')


def user_signup(request): 
        if not request.user.is_authenticated: 
                template_path = 'lib_users/user_signup.html'
                if request.method == 'POST': 
                        form = CustomUserCreationForm(data=request.POST)
                        if form.is_valid(): 
                                form.save()
                                return redirect('dashboard')   
                else : 
                        form = CustomUserCreationForm()
                return render(request, template_path, {'form' : form})
        else : 
                return redirect('dashboard')


def user_logout(request): 
        if request.user.is_authenticated: 
                logout(request)
                messages.success(request, 'You are now logged out!')
                return redirect('login')
        else: 
                return redirect('login')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request): 
        template_path = 'core/home.html'
        return render(request, template_path)

@login_required(login_url='login')
def dashboard(request):
        if request.user.is_authenticated: 
                template_path = 'core/dashboard.html'
                return render(request, template_path)
        


from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import DemoModel, User


class DemoModelForm(forms.ModelForm): 
        class Meta: 
                model = DemoModel
                fields = ['name', 'email', 'password']
                
                labels = {
                        'name' : 'Your Name', 
                        'email' : 'Your Email', 
                        'password' : 'Your Password'
                }

                error_messages = {
                        'name' : {'required' : 'Enter name'},
                        'email' : {'required' : 'Enter email'},
                        'password' : {'required' : 'Enter password'},
                }
                
                widgets = {
                        'name' : forms.TextInput(attrs={'class' : 'demo_class', 'placeholder' : 'Enter Your Name'}),
                        'email' : forms.EmailInput(attrs={'class' : 'demo_email', 'placeholder' : 'Enter Your Email'}),
                        'password' : forms.PasswordInput(attrs={'class' : 'demo_pass', 'placeholder' : 'Enter Your Password'}),
                }
                
                

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', ]
        
        
class UserLoginForm(AuthenticationForm): 
        class Meta: 
                model = User 
                fields = ['username', 'password']
                
                
                
# no use of this model form . To use a form as singup we must use usercreation form or to use login functionality, we must use authentication form 

# class UserModelForm(forms.ModelForm):   
#         class Meta:
#                 model = User 
#                 fields =  ['first_name', 'last_name', 'email', 'bio', 'location']
                
#                 labels = {
#                         'first_name' : 'Your First Name', 
#                         'last_name' : 'Your Last Name', 
#                         'email' : 'Your Email', 
#                         'password' : 'Your Password',
#                         'bio' : 'Your Bio', 
#                         'location' : 'Your Location',
#                 }

#                 # error_messages = {
#                 #         'fistname' : {'required' : 'Enter name'},
#                 #         'email' : {'required' : 'Enter email'},
#                 #         'password' : {'required' : 'Enter password'},
#                 # }
                
#                 widgets = {
#                         'first_name' : forms.TextInput(attrs={'class' : 'demo_class', 'placeholder' : 'Enter Your Name'}),
#                         'email' : forms.EmailInput(attrs={'class' : 'demo_email', 'placeholder' : 'Enter Your Email'}),
#                         'password' : forms.PasswordInput(attrs={'class' : 'demo_pass', 'placeholder' : 'Enter Your Password'}),
#                         'bio' : forms.Textarea(attrs={'class' : 'bio_class', 'placeholder' : 'Enter Your Bio'}),
#                 }




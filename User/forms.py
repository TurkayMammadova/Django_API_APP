from django import forms
from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
User = get_user_model()






class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'User name',
        'class': 'form-control'
        }

    ))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First name',
        'class': 'form-control'
        }

    ))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last name',
        'class': 'form-control'
        }

    ))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'
    
        }

    ))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password1',
        'class': 'form-control'
        }

    ))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password2',
        'class': 'form-control'
        }

     ))
    

       



class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'
    
        }

    ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your password',
        'class': 'form-control'
        }

    ))
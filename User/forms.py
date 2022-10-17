
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
User = get_user_model()

class RegistrationForm(UserCreationForm):
    
    # username = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'User name',
    #     'class': 'form-control'
    #     }

    # ))
    # first_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'First name',
    #     'class': 'form-control'
    #     }

    # ))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'Last name',
    #     'class': 'form-control'
    #     }

    # ))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={
    #     'placeholder': 'Email',
    #     'class': 'form-control'
    
    #     }

    # ))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'placeholder': 'Password1',
    #     'class': 'form-control'
    #     }

    # ))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'placeholder': 'Password2',
    #     'class': 'form-control'
    #     }

    # ))
    class Meta:
        confirm_password = forms.CharField(widget=forms.PasswordInput(attrs = {'class' : 'form-control',
            'placeholder' : 'Confirm Password'}))
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password','image']
        widgets = {
                'username': forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username'
            }),
                'first_name': forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'First Name'
            }),
                'last_name': forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Last Name'
            }),
                'email': forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Email'
            }),
                'password': forms.PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Password'
            })
        }

        def clean(self):
            cleaned_data = super(RegistrationForm,self).clean()
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise ValidationError('Passwords are not equal')




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
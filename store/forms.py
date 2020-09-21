from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(UserCreationForm):
    email = forms.EmailField(label='Email',
                             max_length=120,
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'Enter Email'
                             }))

    password1 = forms.CharField(label='Password',
                                max_length=120,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter Password'}))


class RegisterForm(UserCreationForm):

    username = forms.CharField(label='Your Username',
                                 max_length=120,
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'Enter Username'
                                 }))

    email = forms.EmailField(label='Email',
                             max_length=120,
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'Enter Email'
                             }))
    password1 = forms.CharField(label='Password',
                                 max_length=120,
                                 widget=forms.PasswordInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Enter Password'}))

    password2 = forms.CharField(label='Confirm Your Password',
                                max_length=120,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Enter Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
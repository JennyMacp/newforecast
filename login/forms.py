from django import forms
from django.contrib.auth.models import User

class FormLogin(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(attrs={'class': 'form-style', 'type': 'text', 'id': 'username', 'placeholder': 'Your Username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-style', 'type': 'password', 'id': 'password', 'placeholder': 'Your Password'})
    )
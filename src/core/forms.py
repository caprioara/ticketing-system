from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'input-data'}
        )
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input-data'}
    ))
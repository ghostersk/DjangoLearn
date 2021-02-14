from django import forms
from .models import LoginForm
from django.contrib.auth.forms import AuthenticationForm

class RegUser(forms.ModelForm):

    class Meta:
        model = LoginForm
        fields = ('username', 'alias', 'email', 'password')

class LogUser(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LogUser, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
))
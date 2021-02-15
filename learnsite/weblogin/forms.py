from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    alias = forms.CharField(max_length=30, label='Nickname', help_text='This will be visible for all users.')    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(widget=forms.DateTimeInput(attrs={
            'type': 'date'}), 
            help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'alias', 'birth_date', 'email', 'password1', 'password2', )
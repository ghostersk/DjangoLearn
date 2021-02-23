from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import (authenticate, password_validation)
from .models import *


class UserFormR(forms.ModelForm):
    password1 = forms.CharField(label=_("Password"),strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', }))  

    class Meta:
        model = UserReg
        fields = ('username', 'alias', 'email', 'birth_date', 'password1', 'password2')

def validate_inp(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
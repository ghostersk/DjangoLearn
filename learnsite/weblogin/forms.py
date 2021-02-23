from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import (authenticate, password_validation)
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
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

    # Check if age is more then 18 years
    def check_age(self, birth_date):
        datex = date.fromisoformat(birth_date)
        today = date.today()
        i = today - datex
        # 6575 days ~ 18 years
        if (i.days < 6575):
            return True
        
        return False

        # this function will be used for the validation
    def clean(self):
 
        # data from the form is fetched using super function
        super(UserFormR, self).clean()
         
        # extract the username and alias field from the data
        username = self.cleaned_data.get('username')
        alias = self.cleaned_data.get('alias')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        birth_date = str(self.cleaned_data.get('birth_date'))
 
        # conditions to be met for user input
        if len(username) < 5:
            self._errors['username'] = self.error_class([
                'Minimum 5 characters required.'])   
        
        if len(alias) <5:
            self._errors['alias'] = self.error_class([
                'Alias Should Contain a minimum of 5 characters.'])
        if username in alias:
            self._errors['alias'] = self.error_class([
                'Alias cannot contain username.'])  

        # validate age of user  
        if self.check_age(birth_date):
            raise ValidationError(_('%(value)s is not an even number'),
                params={'value': birth_date},
        )
            self._errors['birth_date'] = self.error_class([
                'Only people 18+ years old are allowed on this website.'])           
        
        # Validate email address
        try:
            validate_email(email)
        except ValidationError as e:
            self._errors['email'] = self.error_class([
                'Please provide valid email address'])
        
                # return any errors if found
        return self.cleaned_data


def validate_inp(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError


class CustomCreationForm(UserCreationForm):
    email =  forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Your password must be 10 characters long, and \n and must not be all alpha numeric'
        self.fields['username'].widget.attrs['placeholder'] = 'Your Unique Desired Username'
        self.fields['password2'].help_text = 'Please make sure that it is same as before'
        self.fields['email'].help_text = "Please enter your genuine email address, we need that for confirmation"

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if(len(password)< 10): raise ValidationError('Please enter at least 10 characters of strings')
        if(password.isalnum()): raise ValidationError('Please enter at least one character that is not alphabet or number')
        return password




        

    



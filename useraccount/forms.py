from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.exceptions import ValidationError
from useraccount.models import UserModel
from django.contrib.auth.models import User


class CustomCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=False)
    age = forms.IntegerField(max_value=120, min_value=5)

    class Meta:
            model = User
            include = "__all__"
            exclude= ('user_permissions','groups', 'is_superuser', 'last_login', 'first_name', 'last_name','is_staff','date_joined', 'is_active',
                      'password')
	

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = 'Your password must be 10 characters long, and \n and must not be all alpha numeric'
        self.fields['username'].widget.attrs['placeholder'] = 'Your Unique Desired Username'
        self.fields['username'].help_text = 'You cannot change your username once set'
        self.fields['password2'].help_text = 'Please make sure that it is same as before'
        self.fields['email'].help_text = "Please enter your genuine email address, we need that for confirmation"

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if(len(password)< 10): raise ValidationError('Please enter at least 10 characters of strings')
        if(password.isalnum()): raise ValidationError('Please enter at least one character that is not alphabet or number')
        return password

class CustomUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=False)
    age = forms.IntegerField(max_value=120, min_value=5)

    class Meta:
            model = UserModel
            include = "__all__"
            exclude= ('date', 'updated_time', 'bmi', 'height', 'weight','user', 'email_confirmed','suggestions')
	

class CustomLoginForm(AuthenticationForm):
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['class'] = 'form-control'
    
    
    
from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = CustomUser
        fields = ['admission_number', 'password']

class LoginForm(forms.Form):
    admission_number = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)  
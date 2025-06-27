from django import forms
from django.db import models
from .models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password', 'role']
        widgets = {
            'role': forms.Select(choices=[('attendee', 'Attendee'), ('organizer', 'Organizer')])
        }
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)





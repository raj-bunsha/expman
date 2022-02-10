from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Account
class RegisterForm(UserCreationForm):
    email=forms.EmailField(max_length=60,help_text="Enter a valid email address")
    class Meta:
        models=Account
        fiels={"email","username","password"}

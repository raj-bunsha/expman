from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Account
class RegisterForm(UserCreationForm):
    email=forms.EmailField(max_length=60,help_text="Enter a valid email address")
    class Meta:
        model=Account
        fields={"email","username","password1","password2"}

    def clean_password2(self):
        password1=self.cleaned_data.get("password1","")
        password2=self.cleaned_data["password2"]
        if password1!=password2:
            raise forms.ValidationError(f"Passwords don't match.")
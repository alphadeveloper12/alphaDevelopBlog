from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.ModelForm):
    # email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'password']
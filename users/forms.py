from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core.validators import validate_fields


class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-field',
            'type': "text",
            'placeholder': 'username',
            'id': 'username'
        }))

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control input-field',
            'type': "password",
            'placeholder': 'Password',
            'id': 'password'
        }),
    )

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-field',
            'type': "text",
            'placeholder': 'username',
            'id': 'username',
        }), validators=[validate_fields])

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control input-field',
            'placeholder': 'Email', 'required': True,
            'type': "email"

        }))

    password1 = forms.CharField(
        strip=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control input-field',
            'placeholder': 'Password', 'type': "password",
        }), validators=[validate_fields])

    password2 = forms.CharField(
        strip=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control input-field',
            'placeholder': 'Password', 'type': "password",
        }), validators=[validate_fields])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

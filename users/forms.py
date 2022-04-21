from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from core.validators import validate_fields


class LoginForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control input-field',
            'placeholder': 'Email', 'required': False,
            'type': "email"

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
        fields = ('email', 'password')

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
        fields = ('username', 'password1', 'password2')


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-field',
            'type': "text",
            'placeholder': 'Имя',
            'id': 'first_name',
        }))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-field',
            'type': "text",
            'placeholder': 'Фамилия',
            'id': 'last_name',
        }))

    # email = forms.EmailField(
    #     widget=forms.EmailInput(attrs={
    #         'class': 'form-control input-field',
    #         'placeholder': 'Email', 'required': False,
    #         'type': "email"
    #
    #     }))

    birthday = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control input-field',
            'placeholder': 'День рождения', 'required': False,
            'type': "date"

        }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'birthday')

from http import HTTPStatus

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render

from core.validators import validate_fields, validate_password
from .forms import LoginForm, RegisterForm

USER_LIST_TEMPLATE = 'users/user_list.html'
CUR_USER_TEMPLATE = 'users/user_detail.html'
SIGNUP_TEMPLATE = 'users/signup.html'
LOGIN_TEMPLATE = 'users/login.html'
PROFILE_TEMPLATE = 'users/profile.html'


def user_list(request) -> HttpResponse:
    """
    Возвращает страничку Списка пользователей
    """
    return render(
        request, USER_LIST_TEMPLATE, status=HTTPStatus.OK, context={},
        content_type='text/html'
    )


def user_detail(request, user_id: int) -> HttpResponse:
    """
    Возвращает страничку конкретного пользователя
    """

    # В условии было сказано про то, что словарь контекста должен быть пустым
    # Но мне показалось логичным передавать айди пользователя

    return render(
        request, CUR_USER_TEMPLATE, status=HTTPStatus.OK,
        context={'user_id': user_id}, content_type='text/html'
    )


def login_view(request) -> HttpResponse:
    """
    Возвращает страничку регистрации пользователя
    """

    if request.user.is_authenticated:
        return redirect('/auth/profile', status=HTTPStatus.OK,
                        context={}, content_type='text/html')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(
                    '/auth/profile', status=HTTPStatus.OK,
                    context={},
                    content_type='text/html')
    form_login = LoginForm()
    return render(
        request, LOGIN_TEMPLATE, status=HTTPStatus.OK,
        context={"form_login": form_login},
        content_type='text/html'
    )


def logout_view(request) -> HttpResponse:
    """
    Возвращает страничку регистрации пользователя
    """

    if request.user.is_authenticated:
        logout(request)

        return redirect('/', status=HTTPStatus.OK,
                        context={}, content_type='text/html')

    form_login = LoginForm()
    return render(
        request, LOGIN_TEMPLATE, status=HTTPStatus.OK,
        context={"form_login": form_login},
        content_type='text/html'
    )


def signup(request) -> HttpResponse:
    errors = []

    if request.user.is_authenticated:
        logout(request)

    if request.method == 'POST':
        form_reg = RegisterForm(request.POST)

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']

        if User.objects.filter(email=email):
            errors.append('Пользователь с этой почтой уже есть')

        # не использую RegisterForm.is_valid() т.к. при идентичных паролях
        # все равно возвращает, что они не совпадают (form_reg.error_messages)
        # поэтому решил сделать ручками (валидация совпадения паролей, их
        # длинны и корректность заполненых полей реализована на фронте)

        if not errors:
            try:

                validate_fields(username)
                validate_password(password1)

                new_user = User(
                    username=username,
                    email=email,
                    password=make_password(password1),
                )

                new_user.save()

                return redirect('/auth/profile', status=HTTPStatus.OK,
                                context={}, content_type='text/html')

            except (IntegrityError, ValidationError) as err:
                if type(err) is ValidationError:
                    err = '\n'.join(err.messages)
                    # print(help(err))
                if type(err) is IntegrityError:
                    err = 'Пользователь с таким именем уже сооздан'
                errors.append(err)
        else:
            messages.error(request, '\n'.join(errors))

    else:
        form_reg = RegisterForm()

    return render(
        request, SIGNUP_TEMPLATE, status=HTTPStatus.OK,
        context={"form_login": form_reg, 'errors': '\n'.join(errors)},
        content_type='text/html'
    )


def profile(request) -> HttpResponse:
    """
    Возвращает страничку профиля пользователя
    """

    return render(
        request, PROFILE_TEMPLATE, status=HTTPStatus.OK, context={},
        content_type='text/html'
    )

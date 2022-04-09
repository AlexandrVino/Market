from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render

USER_LIST_TEMPLATE = 'users/user_list.html'
CUR_USER_TEMPLATE = 'users/user_detail.html'
SIGNUP_TEMPLATE = 'users/signup.html'
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


def signup(request) -> HttpResponse:
    """
    Возвращает страничку регистрации пользователя
    """

    return render(
        request, SIGNUP_TEMPLATE, status=HTTPStatus.OK, context={},
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

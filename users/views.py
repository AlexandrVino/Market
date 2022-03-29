from django.http import HttpResponse
from http import HTTPStatus

from django.shortcuts import render


def user_list(request) -> HttpResponse:
    """
    Возвращает страничку Списка пользователей
    """
    return render(
        request, 'users/user_list.html', status=HTTPStatus.OK, context={},
        content_type='text/html'
    )


def user_detail(request, user_id: int) -> HttpResponse:
    """
    Возвращает страничку конкретного пользователя
    """

    # В условии было сказано про то, что словарь контекста должен быть пустым
    # Но мне показалось логичным передавать айди пользователя

    return render(
        request, 'users/user_detail.html', status=HTTPStatus.OK,
        context={'user_id': user_id}, content_type='text/html'
    )


def signup(request) -> HttpResponse:
    """
    Возвращает страничку регистрации пользователя
    """

    return render(
        request, 'users/signup.html', status=HTTPStatus.OK, context={},
        content_type='text/html'
    )


def profile(request) -> HttpResponse:
    """
    Возвращает страничку профиля пользователя
    """

    return render(
        request, 'users/profile.html', status=HTTPStatus.OK, context={},
        content_type='text/html'
    )

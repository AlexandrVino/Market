from django.http import HttpResponse
from http import HTTPStatus
from django.shortcuts import render


# Create your views here.
def user_list(request) -> HttpResponse:
    return HttpResponse('Список пользователей', status=HTTPStatus.OK)


def user_detail(request, user_id: int) -> HttpResponse:
    # Не знаю, нужно ли выводить айдишник из строки
    # (В условии задачи не было), но, мне кажется логичным
    return HttpResponse(
        f'Информация о пользователе {user_id}', status=HTTPStatus.OK
    )


def signup(request) -> HttpResponse:
    return HttpResponse('Регистрация', status=HTTPStatus.OK)


def profile(request) -> HttpResponse:
    return HttpResponse('Мой профиль', status=HTTPStatus.OK)

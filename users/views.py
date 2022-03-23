from django.http import HttpResponse
from http import HTTPStatus


def user_list(request) -> HttpResponse:
    """
    Возвращает страничку Списка пользователей
    """

    return HttpResponse('Список пользователей', status=HTTPStatus.OK)


def user_detail(request, user_id: int) -> HttpResponse:
    """
    Возвращает страничку конкретного пользователя
    """

    return HttpResponse(
        f'Информация о пользователе {user_id}', status=HTTPStatus.OK
    )


def signup(request) -> HttpResponse:
    """
    Возвращает страничку регистрации пользователя
    """

    return HttpResponse('Регистрация', status=HTTPStatus.OK)


def profile(request) -> HttpResponse:
    """
    Возвращает страничку профиля пользователя
    """

    return HttpResponse('Мой профиль', status=HTTPStatus.OK)

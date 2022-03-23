from django.http import HttpResponse
from http import HTTPStatus


def home(request) -> HttpResponse:
    """
    Возвращает главную страничку сайта
    """

    return HttpResponse('Главная', status=HTTPStatus.OK)

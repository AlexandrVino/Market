from django.http import HttpResponse
from http import HTTPStatus


def description(request) -> HttpResponse:
    """
    Возвращает страничку информации о проекте
    """

    return HttpResponse('О проекте', status=HTTPStatus.OK)

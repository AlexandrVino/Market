from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render

ABOUT_TEMPLATE = 'about/description.html'


def description(request) -> HttpResponse:
    """
    Возвращает страничку информации о проекте
    """

    return render(
        request, ABOUT_TEMPLATE, status=HTTPStatus.OK, context={},
        content_type='text/html'
    )

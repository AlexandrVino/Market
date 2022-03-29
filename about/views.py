from django.http import HttpResponse
from http import HTTPStatus

from django.shortcuts import render


def description(request) -> HttpResponse:
    """
    Возвращает страничку информации о проекте
    """

    return render(
        request, 'about/description.html', status=HTTPStatus.OK, context={},
        content_type='text/html'
    )

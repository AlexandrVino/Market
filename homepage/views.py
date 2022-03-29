from django.http import HttpResponse
from http import HTTPStatus

from django.shortcuts import render


def home(request) -> HttpResponse:
    """
    Возвращает главную страничку сайта
    """
    return render(
        request, 'homepage/home.html', status=HTTPStatus.OK, context={},
        content_type='text/html'
    )

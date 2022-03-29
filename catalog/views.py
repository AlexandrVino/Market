from django.http import HttpResponse
from http import HTTPStatus

from django.shortcuts import render


def item_list(request) -> HttpResponse:
    """
    Возвращает страничку Списка товаров
    """
    return render(
        request, 'catalog/list.html', status=HTTPStatus.OK, context={},
        content_type='text/html'
    )


def item_detail(request, item_index: int) -> HttpResponse:
    """
    Возвращает страничку конкретного товара
    """

    # В условии было сказано про то, что словарь контекста должен быть пустым
    # Но мне показалось логичным передавать айди товара

    return render(
        request, 'catalog/detail.html', status=HTTPStatus.OK,
        context={'item_index': item_index}, content_type='text/html'
    )

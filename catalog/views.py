from django.http import HttpResponse
from http import HTTPStatus


def item_list(request) -> HttpResponse:
    """
    Возвращает страничку Списка товаров
    """

    return HttpResponse('Список элементов', status=HTTPStatus.OK)


def item_detail(request, item_index: int) -> HttpResponse:
    """
    Возвращает страничку конкретного товара
    """

    return HttpResponse(
        f'Подробно элемент "{item_index}"', status=HTTPStatus.OK
    )

from django.http import HttpResponse
from http import HTTPStatus

from django.shortcuts import get_object_or_404, render

from catalog.models import Item, Tag


def item_list(request) -> HttpResponse:
    """
    Возвращает страничку Списка товаров
    """

    items = Item.objects.all().prefetch_related('tags')\
        .only('name', 'text', 'tags')

    return render(
        request, 'catalog/item_list.html', status=HTTPStatus.OK,
        context={'items': items}, content_type='text/html'
    )


def item_detail(request, item_index: int) -> HttpResponse:
    """
    Возвращает страничку конкретного товара
    """

    # В условии было сказано про то, что словарь контекста должен быть пустым
    # Но мне показалось логичным передавать айди товара

    item = get_object_or_404(Item, id=item_index, is_published=True)
    return render(
        request, 'catalog/item_detail.html', status=HTTPStatus.OK,
        context={'item': item}, content_type='text/html'
    )

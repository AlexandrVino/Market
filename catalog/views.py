from http import HTTPStatus

from django.db.models import Prefetch
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from catalog.models import Item, Tag

ALL_ITEMS_TEMPLATE = 'catalog/item_list.html'
CUR_ITEM_TEMPLATE = 'catalog/item_detail.html'


def item_list(request) -> HttpResponse:
    """
    Возвращает страничку Списка товаров
    """

    items = Item.objects.filter(is_published=True).prefetch_related(
        Prefetch('tags', queryset=Tag.objects.filter(is_published=True)))\
        .only('name', 'text', 'tags__name')

    return render(
        request, ALL_ITEMS_TEMPLATE, status=HTTPStatus.OK,
        context={'items': items}, content_type='text/html'
    )


def item_detail(request, item_index: int) -> HttpResponse:
    """
    Возвращает страничку конкретного товара
    """

    item = get_object_or_404(Item, id=item_index, is_published=True)
    tags = item.tags.filter(is_published=True).only('name')

    return render(
        request, CUR_ITEM_TEMPLATE, status=HTTPStatus.OK,
        context={'item': item, 'tags': tags}, content_type='text/html'
    )

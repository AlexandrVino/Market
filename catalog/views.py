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
        Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only(
            'name'))).only('name', 'text', 'tags__name')

    return render(
        request, ALL_ITEMS_TEMPLATE, status=HTTPStatus.OK,
        context={'items': items}, content_type='text/html'
    )


def item_detail(request, item_index: int) -> HttpResponse:
    """
    Возвращает страничку конкретного товара
    """

    item = get_object_or_404(Item.objects.select_related('category').filter(
        category__is_published=True).only('name', 'text',
                                          'category__name').prefetch_related(
        Prefetch('tags', queryset=Tag.objects.filter(is_published=True).only(
            'name'))), id=item_index, is_published=True)

    return render(
        request, CUR_ITEM_TEMPLATE, status=HTTPStatus.OK,
        context={'item': item}, content_type='text/html'
    )

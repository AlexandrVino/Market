from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from catalog.models import Item, Tag

ALL_ITEMS_TEMPLATE = 'catalog/item_list.html'
CUR_ITEM_TEMPLATE = 'catalog/item_detail.html'


def item_list(request) -> HttpResponse:
    """
    Возвращает страничку Списка товаров
    """

    items = Item.manager.join_tags(
        Tag, None, 'name', 'text', 'tags__name', 'category__is_published',
        'category__name', is_published=True)
    data = {}

    for item in items:

        if not item.category.is_published:
            continue

        if data.get(item.category.name) is None:
            data[item.category.name] = []
        data[item.category.name].append(item)

    return render(
        request, ALL_ITEMS_TEMPLATE, status=HTTPStatus.OK,
        context={'categories': data}, content_type='text/html'
    )


def item_detail(request, item_index: int) -> HttpResponse:
    """
    Возвращает страничку конкретного товара
    """

    item = get_object_or_404(
        Item.manager.join_tag(
            Tag, 'name', 'text', 'tags', 'category', is_published=True),
        id=item_index, is_published=True)

    return render(
        request, CUR_ITEM_TEMPLATE, status=HTTPStatus.OK,
        context={'item': item}, content_type='text/html'
    )

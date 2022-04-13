from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from catalog.models import Item, Tag
from rating.models import Rating

ALL_ITEMS_TEMPLATE = 'catalog/item_list.html'
CUR_ITEM_TEMPLATE = 'catalog/item_detail.html'


def item_list(request) -> HttpResponse:
    """
    Возвращает страничку Списка товаров
    """

    items = Item.manager.join_tags(
        Tag, None, 'name', 'text', 'tags__name',
        'category__name', is_published=True)

    return render(
        request, ALL_ITEMS_TEMPLATE, status=HTTPStatus.OK,
        context={
            'items': items,
            'range': range(len(items))
        },
        content_type='text/html'
    )


def item_detail(request, item_index: int) -> HttpResponse:
    """
    Возвращает страничку конкретного товара
    """

    item = get_object_or_404(
       Item.manager.join_tag(
            Tag, 'name', 'text', 'tags__name', 'category__name',
            is_published=True), id=item_index, is_published=True)
    rating = Rating.manager.filter(item=item).only('star')

    if any(rating):
        rating = list(map(lambda x: x.star, rating))
        rating = f'{sum(rating)/len(rating)} звезд/{len(rating)} оценок'

    return render(
        request, CUR_ITEM_TEMPLATE, status=HTTPStatus.OK,
        context={'item': item, 'rating': rating if rating else ''},
        content_type='text/html'
    )

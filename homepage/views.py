from http import HTTPStatus
from random import sample

from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Item, Tag

HOMEPAGE_TEMPLATE = 'homepage/home.html'
ITEMS_COUNT = 4


def home(request) -> HttpResponse:
    """
    Возвращает главную страничку сайта
    """

    ides = list(Item.manager.get_objects_with_filter(
        is_published=True).values_list('id', flat=True))

    if len(ides) > ITEMS_COUNT:
        ides = sample(ides, ITEMS_COUNT)

    items = Item.manager.join_tags(
        Tag, None, 'name', 'text', 'tags__name', 'upload',
        'category__name', is_published=True, pk__in=ides)

    return render(
        request, HOMEPAGE_TEMPLATE, status=HTTPStatus.OK,
        context={'items': items, 'range': range(len(items))},
        content_type='text/html'
    )

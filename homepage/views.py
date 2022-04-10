from http import HTTPStatus
from random import sample

from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Item, Tag

HOMEPAGE_TEMPLATE = 'homepage/home.html'
ITEMS_COUNT = 3


def home(request) -> HttpResponse:
    """
    Возвращает главную страничку сайта
    """

    ides = list(Item.manager.get_objects_with_filter(
        is_published=True).values_list('id', flat=True))

    if len(ides) > ITEMS_COUNT:
        ides = sample(ides, ITEMS_COUNT)

    items = Item.manager.join_tags(
        Tag, None, 'name', 'text', 'tags__name', 'category__is_published',
        'category__name', is_published=True, pk__in=ides)
    data = {}

    for item in items:

        if not item.category.is_published:
            continue

        if data.get(item.category.name) is None:
            data[item.category.name] = []
        data[item.category.name].append(item)

    return render(
        request, HOMEPAGE_TEMPLATE, status=HTTPStatus.OK,
        context={'data': data},
        content_type='text/html'
    )

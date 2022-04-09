from http import HTTPStatus
from random import sample

from django.db.models import Prefetch
from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Item, Tag

HOMEPAGE_TEMPLATE = 'homepage/home.html'
ITEMS_COUNT = 3


def home(request) -> HttpResponse:
    """
    Возвращает главную страничку сайта
    """

    ides = list(Item.objects.filter(is_published=True)
                .values_list('id', flat=True))

    if len(ides) > ITEMS_COUNT:
        ides = sample(ides, ITEMS_COUNT)

    items = Item.objects.filter(
        is_published=True,
        pk__in=ides).prefetch_related(
        Prefetch('tags', queryset=Tag.objects.filter(is_published=True)))\
        .only('name', 'text', 'tags__name')

    return render(
        request, HOMEPAGE_TEMPLATE, status=HTTPStatus.OK,
        context={'items': items},
        content_type='text/html'
    )

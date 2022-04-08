from random import choice, choices, randint, sample

from django.http import HttpResponse
from http import HTTPStatus

from django.shortcuts import render

from catalog.models import Item, Tag


def home(request) -> HttpResponse:
    """
    Возвращает главную страничку сайта
    """

    items = Item.join_tags(
        Item.filter(Item.get_all(), is_published=True,
                    pk__in=sample(
                        list(Item.get_all().values_list('id', flat=True)), 3)
                    ), 'name', 'text', 'tags')

    return render(
        request, 'homepage/home.html', status=HTTPStatus.OK,
        context={'items': items},
        content_type='text/html'
    )

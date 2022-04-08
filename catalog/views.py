from django.http import HttpResponse
from http import HTTPStatus

from django.shortcuts import get_object_or_404, render

from catalog.models import Category, Item, Tag


def item_list(request) -> HttpResponse:
    """
    Возвращает страничку Списка товаров
    """

    items = Item.join_tags(Item.get_all(), 'name', 'text', 'tags')
    categories = Category.sorted(Category.join_items(
        Category.filter(Category.get_all(), item__in=items)))

    return render(
        request, 'catalog/item_list.html', status=HTTPStatus.OK,
        context={'categories': categories}, content_type='text/html'
    )


def item_detail(request, item_index: int) -> HttpResponse:
    """
    Возвращает страничку конкретного товара
    """

    item = get_object_or_404(Item, id=item_index, is_published=True)
    return render(
        request, 'catalog/item_detail.html', status=HTTPStatus.OK,
        context={'item': item}, content_type='text/html'
    )

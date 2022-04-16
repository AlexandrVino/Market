from http import HTTPStatus

from django.db.models import Avg, Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Item, Tag
from rating.forms import AddRate
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

    form = AddRate(request.POST)

    if form.is_valid():
        if not request.user.is_authenticated:
            return redirect('login', content_type='text/html')

        rate = form.cleaned_data['star']

        cur_rate, _ = Rating.manager.get_or_create(
            user_id=request.user.id, item_id=item_index)
        cur_rate.star = rate
        cur_rate.save()

        return redirect('curr_item', item_index=item_index)

    item = get_object_or_404(
        Item.manager.join_tag(
            Tag, 'name', 'text', 'tags__name', 'category__name',
            is_published=True), id=item_index, is_published=True)

    rating = Rating.manager.filter(item=item).exclude(star=0).aggregate(
        Avg('star'), Count('star'))

    return render(
        request, CUR_ITEM_TEMPLATE, status=HTTPStatus.OK,
        context={'item': item, 'form': form,
                 'rating': rating if rating['star__avg'] else ''},
        content_type='text/html'
    )

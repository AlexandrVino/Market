from django.http import HttpResponse
from http import HTTPStatus
from django.shortcuts import render


# Create your views here.
def item_list(request) -> HttpResponse:
    return HttpResponse('Список элементов', status=HTTPStatus.OK)


def item_detail(request, item_index: int) -> HttpResponse:
    # Не знаю, нужно ли выводить индекс элимена из строки (В условии задачи не было), но, мне кажется логичным
    return HttpResponse(f'Подробно элемент "{item_index}"', status=HTTPStatus.OK)

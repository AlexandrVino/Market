from django.http import HttpResponse
from http import HTTPStatus
from django.shortcuts import render


# Create your views here.
def description(request) -> HttpResponse:
    return HttpResponse('О проекте', status=HTTPStatus.OK)


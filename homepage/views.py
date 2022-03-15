from django.http import HttpResponse
from http import HTTPStatus
from django.shortcuts import render


# Create your views here.
def home(request) -> HttpResponse:
    return HttpResponse('Главная', status=HTTPStatus.OK)

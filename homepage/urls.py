from django.contrib import admin
from django.urls import path

from homepage.views import home

urlpatterns = [
    path('', home),
]

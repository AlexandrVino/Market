from django.contrib import admin
from django.urls import path

from about.views import description

urlpatterns = [
    path('', description)
]
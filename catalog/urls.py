from django.contrib import admin
from django.urls import path

from catalog.views import *

urlpatterns = [
    path('', item_list),
    path('<int:item_index>', item_detail),
]

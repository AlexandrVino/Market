from django.urls import path

from catalog.views import item_list, item_detail

urlpatterns = [
    path('', item_list),
    path('<int:item_index>', item_detail),
]

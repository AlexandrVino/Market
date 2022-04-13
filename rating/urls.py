from django.urls import path

from rating.views import add_rate

urlpatterns = [
    path('add/<int:item_index>/', add_rate),
]

from django.urls import path

from catalog.views import ItemListView, ItemDetailView

urlpatterns = [
    path('', ItemListView.as_view(), name='catalog'),
    path('<int:pk>/', ItemDetailView.as_view(), name='curr_item'),
]

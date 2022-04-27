from django.urls import path

from homepage.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]

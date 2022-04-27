from django.urls import path

from about.views import DescriptionView

urlpatterns = [
    path('', DescriptionView.as_view(), name='about')
]

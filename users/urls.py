from django.contrib import admin
from django.urls import path

from users.views import *

urlpatterns = [
    path('users', user_list),
    path('users/<int:user_id>', user_detail),
    path('signup', signup),
    path('profile', profile)
]

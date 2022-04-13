from django.urls import path

from users.views import (login_view, logout_view, profile, signup, user_detail,
                         user_list)

urlpatterns = [
    path('users', user_list),
    path('users/<int:user_id>', user_detail),
    path('signup', signup),
    path('login', login_view),
    path('logout', logout_view),
    path('profile', profile)
]

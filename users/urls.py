from django.urls import path

from users.views import (login_view, logout_view, profile, signup, user_detail,
                         user_list)

urlpatterns = [
    path('users', user_list, name='users'),
    path('users/<int:user_id>', user_detail),
    path('signup', signup, name='signup'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('profile', profile, name='profile')
]

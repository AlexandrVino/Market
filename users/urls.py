from django.urls import path

from users.views import user_list, user_detail, signup, profile

urlpatterns = [
    path('users', user_list),
    path('users/<int:user_id>', user_detail),
    path('signup', signup),
    path('profile', profile)
]

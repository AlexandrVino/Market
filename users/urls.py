from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView,
    PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView,
    PasswordResetView
)
from django.urls import path

from users.views import (profile, signup, user_detail, user_list)

urlpatterns = [

    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),

    path('signup/', signup, name='signup'),

    path('password_change/',
         PasswordChangeView.as_view(
             template_name='users/password_change_form.html'),
         name='password_change'),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(
             template_name='users/password_change_done.html'),
         name='password_change_done'),

    path('password_reset/',
         PasswordResetView.as_view(
             email_template_name='users/password_reset_email.html',
             template_name='users/password_reset_form.html'
         ),
         name='password_reset'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('users/', user_list, name='users'),
    path('users/<int:user_id>', user_detail, name='user_detail'),

    # path('login', login_view, name='login'),
    # path('logout', logout_view, name='logout'),

    path('profile/', profile, name='profile')
]

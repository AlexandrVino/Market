from django.contrib.auth.views import (
    LogoutView, PasswordChangeDoneView, PasswordChangeView,
    PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView,
    PasswordResetView
)
from django.urls import path

from users.views import (AcitvateView, ProfileView, SignupView, UserDetailView,
                         UserListView, LoginWithEmailView)

urlpatterns = [

    # path('login/',
    #      LoginView.as_view(template_name='users/login_with_username.html'),
    #      name='login'),

    path('login/', LoginWithEmailView.as_view(), name='login'),

    path('logout/',
         LogoutView.as_view(template_name='users/logout.html'),
         name='logout'),

    path('signup/', SignupView.as_view(), name='signup'),
    path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/'
         '(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         AcitvateView.as_view(), name='activate'),

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

    path('users/', UserListView.as_view(), name='users'),
    path('users/<int:user_id>', UserDetailView.as_view(), name='user_detail'),

    # path('login', login_view, name='login'),
    # path('logout', logout_view, name='logout'),

    path('profile/', ProfileView.as_view(), name='profile')
]

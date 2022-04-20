import mimetypes

from django.contrib import admin
from django.urls import include, path

mimetypes.add_type("application/javascript", ".js", True)

urlpatterns = [

    path('admin/', admin.site.urls),

    # urls for my apps
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about.urls')),

    # path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('users.urls')),
    # path("auth/", include("account.urls")),

    path('__debug__/', include('debug_toolbar.urls')),
]

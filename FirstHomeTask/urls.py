from django.contrib import admin
from django.templatetags.static import static
from django.urls import path, include

import mimetypes

mimetypes.add_type("application/javascript", ".js", True)

urlpatterns = [

    path('admin/', admin.site.urls),

    # urls for my apps
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about.urls')),
    path('auth/', include('users.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
]

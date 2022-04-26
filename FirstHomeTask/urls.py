import mimetypes

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from FirstHomeTask import settings

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

]

if settings.DEBUG:
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

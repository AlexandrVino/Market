from django.contrib import admin
from rating.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('star', 'item', 'user')
    list_display_links = ('star', 'item', 'user')

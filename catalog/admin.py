from django.contrib import admin

# Register your models here.
from catalog.models import (Item)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'text')
    list_editable = ('is_published',)
    list_display_links = ('text',)

    # filter_horizontal = ('', )

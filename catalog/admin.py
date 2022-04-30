from django.contrib import admin

from catalog.models import Category, ImageGallery, Item


class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "image_tmb")
    list_editable = ("is_published",)
    list_display_links = ("name",)
    filter_horizontal = ("tags",)

    inlines = [ImageGalleryInline]

    def save_related(self, request, form, formsets, change):
        # в этой функции он сохраняет релатид модели
        super().save_related(request, form, formsets, change)


class TagAdmin(admin.ModelAdmin):
    list_display = ("is_published", "slug")
    list_editable = ("is_published",)
    list_display_links = ("slug",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("is_published", "slug", "weight")
    list_editable = ("is_published",)
    list_display_links = ("slug",)

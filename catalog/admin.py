from django.contrib import admin
from django.forms import ValidationError

from catalog.models import Category, ImageGallery, Item, Tag

from django.forms.models import BaseInlineFormSet


class ImageGalleryFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        main_image_count = sum(map(
            lambda x: 1 if x.cleaned_data.get("is_main", False) else 0,
            self.forms
        ))

        print(main_image_count)

        if main_image_count > 1:
            raise ValidationError("Только одна картинка может быть главной")


class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery
    formset = ImageGalleryFormSet


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "is_published", "image_tmb")
    list_editable = ("is_published",)
    list_display_links = ("name",)
    filter_horizontal = ("tags",)

    inlines = [ImageGalleryInline]

    def clean(self):
        super().clean()

    def save_related(self, request, form, formsets, change):
        # в этой функции он сохраняет релатид модели
        super().save_related(request, form, formsets, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("is_published", "slug")
    list_editable = ("is_published",)
    list_display_links = ("slug",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("is_published", "slug", "weight")
    list_editable = ("is_published",)
    list_display_links = ("slug",)

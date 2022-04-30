from random import sample

from django.views.generic.list import ListView

from catalog.models import ImageGallery, Item, Tag

HOMEPAGE_TEMPLATE = "homepage/home.html"
ITEMS_COUNT = 4


class HomeView(ListView):
    """Возвращает главную страничку сайта"""

    template_name = HOMEPAGE_TEMPLATE
    model = Item
    context_object_name = "items"

    def get_queryset(self):
        ides = list(
            Item.manager.get_objects_with_filter(
                is_published=True).values_list(
                "id", flat=True
            )
        )

        if len(ides) > ITEMS_COUNT:
            ides = sample(ides, ITEMS_COUNT)

        return Item.manager.join_tags(
            ImageGallery,
            Tag,
            None,
            "name",
            "text",
            "tags__name",
            "category__name",
            is_published=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["range"] = range(len(context["items"]))
        return context

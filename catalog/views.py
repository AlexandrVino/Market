from django.db.models import Avg, Count
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from catalog.models import Item, ItemGallery, Tag
from rating.forms import AddRate
from rating.models import Rating

ALL_ITEMS_TEMPLATE = "catalog/item_list.html"
CUR_ITEM_TEMPLATE = "catalog/item_detail.html"


class ItemListView(ListView):
    """Возвращает страничку Списка товаров"""

    template_name = ALL_ITEMS_TEMPLATE
    context_object_name = "items"

    def get_queryset(self):
        return Item.manager.join_tags(
            Tag,
            None,
            "name",
            "text",
            "tags__name",
            "main_image",
            "category__name",
            is_published=True,
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["range"] = range(len(context["items"]))
        return context


class ItemDetailView(DetailView):
    """Возвращает страничку конкретного товара"""

    template_name = CUR_ITEM_TEMPLATE
    model = Item
    form_class = AddRate
    context_object_name = "item"

    def get_queryset(self, **kwargs):
        return Item.manager.join_tag(
            Tag,
            "name",
            "text",
            "tags__name",
            "category__name",
            "main_image",
            is_published=True,
        ).filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()

        rating = (
            Rating.manager.filter(item=context["item"])
            .exclude(star=0)
            .aggregate(Avg("star"), Count("star"))
        )

        gallery = ItemGallery.manager.get_objects_with_filter(item_id=context["item"].id)

        context["rating"] = rating if rating["star__avg"] else ""

        context["gallery"] = gallery if gallery else []
        context["range"] = range(len(gallery))

        return context

    def post(self, request, *args, **kwargs):
        pk = self.get_object().pk
        form = self.form_class(request.POST)

        if form.is_valid():
            if not request.user.is_authenticated:
                return redirect("login", content_type="text/html")

            rate = form.cleaned_data["star"]

            cur_rate, _ = Rating.manager.get_or_create(
                user_id=request.user.id, item_id=pk
            )
            cur_rate.star = rate
            cur_rate.save()

            return redirect("curr_item", pk=pk)

        context = self.get_context_data()
        context["form"] = form
        return render(request, self.template_name, context)

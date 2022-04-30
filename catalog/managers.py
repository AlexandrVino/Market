from django.contrib.auth import get_user_model
from django.db.models import Prefetch

from core.managers import BaseManager

User = get_user_model()


class ItemsManager(BaseManager):
    def join_tag(self, model, *args, **kwargs):
        return (
            self.model.manager.select_related("category")
            .filter(category__is_published=True)
            .prefetch_related(
                Prefetch("tags", queryset=model.manager.filter(**kwargs).only(
                    "name"))
            )
            .only(*args)
        )

    def join_tags(self, model, items=None, *args, **kwargs):
        if items is None:
            items = self.get_objects_with_filter(**kwargs)

        return (
            items.select_related("category")
            .filter(category__is_published=True)
            .order_by("category")
            .prefetch_related(
                Prefetch(
                    "tags",
                    queryset=model.manager.filter(is_published=True).only(
                        "name"),
                )
            )
            .only(*args)
        )

    def join_users(self, user, items=None, *args, **kwargs):
        if items is None:
            items = self.get_objects_with_filter(**kwargs)

        return (
            items.select_related("category")
            .filter(category__is_published=True)
            .order_by("category")
            .prefetch_related(
                Prefetch(
                    "users",
                    queryset=User.objects.filter(rating__user=user)
                    .only("name"),
                )
            )
            .only(*args)
        )

    def get_favorite(self, user, tag_model, *args, **kwargs):

        return self.join_tags(
            tag_model,
            items=self.get_objects_with_filter(
                rating__user__exact=user, rating__star=5, **kwargs
            ),
        )


class CategoriesManager(BaseManager):
    def join_items(self, categories=None, *args, **kwargs):
        if categories is None:
            categories = self.get_objects_with_filter(**kwargs)
        return categories.prefetch_related("item_set").only(*args)

    def sorted(self, categories=None, **kwargs) -> list:
        if categories is None:
            categories = self.get_objects_with_filter(**kwargs)

        return sorted(categories, key=lambda x: x.weight)


class ItemGalleryManager(BaseManager):
    """
    Пока класс ничего не делает, но во время разработки
    добавится методы, которые будет он будет содержать
    """

    def join_images(self, galleries=None, *args, **kwargs):
        if galleries is None:
            galleries = self.get_objects_with_filter(**kwargs)
        return galleries.prefetch_related(
            Prefetch("item_gallery")
        ).only(*args)

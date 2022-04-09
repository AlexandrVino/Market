from django.db.models import Prefetch

from core.managers import BaseManager


class ItemsManager(BaseManager):

    def join_tag(self, model, *args, **kwargs):
        return self.model.manager.select_related('category').filter(
            category__is_published=True).prefetch_related(
            Prefetch(
                'tags',
                queryset=model.manager.filter(**kwargs))).only(*args)

    def join_tags(self, model, items=None, *args, **kwargs):
        if items is None:
            items = self.get_objects_with_filter(**kwargs)

        return items.select_related('category').prefetch_related(
            Prefetch(
                'tags',
                queryset=model.manager.filter(is_published=True))).only(
            *args)


class CategoriesManager(BaseManager):
    def join_items(self, categories=None, *args, **kwargs):
        if categories is None:
            categories = self.get_objects_with_filter(**kwargs)
        return categories.prefetch_related('item_set').only(
            *args)

    def sorted(self, categories=None, **kwargs) -> list:
        if categories is None:
            categories = self.get_objects_with_filter(**kwargs)

        return sorted(categories, key=lambda x: x.weight)

from core.managers import BaseManager


class RatingManager(BaseManager):
    def get_item_rating(self, rate=None, *args, **kwargs):
        if not rate:
            return self.get_objects_with_filter(**kwargs)

        return rate.filter(*args, **kwargs)

    def join_item(self, item, *args, **kwargs):
        rating = self.join_items([item[0]])
        return [rating] if rating else item

    def join_items(self, items, *args, **kwargs):
        return (
            self.model.manager.select_related("item")
            .filter(item__in=items)
            .only("star", "item")
        )

from django.contrib.auth import get_user_model
from django.db import models

from catalog.models import Item
from rating.managers import RatingManager

User = get_user_model()


class Rating(models.Model):
    """
    Модель оценки товара
    """

    # если удалили товар, то удаляем все его оценки
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        default=None,
        help_text="Пожалуйста, укажите товар",
        related_name='item_rating',
    )

    manager = RatingManager()

    # если удалили пользователя, то удаляем все его оценки
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    star = models.SmallIntegerField(
        blank=True,
        default=0,
        choices=(
            (1, "Ненависть"),
            (2, "Неприязнь"),
            (3, "Нейтрально"),
            (4, "Обожание"),
            (5, "Любовь"),
            (0, "Не могу сказать"),
        ),
        help_text="Поставьте рейтинг от 1 до 5",
    )

    def __str__(self):
        return f"Оценка {self.item}"

    class Meta:
        # Устанавливаем уникальноть,
        # что связка (товар - юзер) может встречаться один раз
        constraints = [
            models.UniqueConstraint(fields=["user", "item"], name="unique")]

        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"

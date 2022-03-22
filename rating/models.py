from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from catalog.models import Item


class Rating(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.DO_NOTHING, default=None,
        help_text='Пожалуйста, укажите товар'
    )

    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, default=None)

    star = models.SmallIntegerField(validators=[MaxValueValidator(5),
                                                MinValueValidator(0)],
                                    help_text='Поставьте рейтинг от 1 до 5')

    class Meta:

        # Устанавливаем уникальноть,
        # что связка (товар - юзер) может встречаться один раз

        unique_together = ('item', 'user')

        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

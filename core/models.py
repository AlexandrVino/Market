from django.core.validators import validate_slug
from django.db import models


class Base(models.Model):
    """
    Базовый абстрактный класс моделей
    """

    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано')

    class Meta:
        abstract = True


class BaseSlug(Base):
    """
    Базовый абстрактный класс моделей (вместе с полем слага)
    """

    slug = models.SlugField(
        max_length=200, unique=True,
        help_text='Максимум 200 символов', verbose_name='Название')

    class Meta:
        abstract = True

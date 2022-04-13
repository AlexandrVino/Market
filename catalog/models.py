from django.core.validators import MinValueValidator
from django.db import models

from catalog.managers import CategoriesManager, ItemsManager
from core.managers import BaseManager
from core.models import Base, BaseSlug
from core.validators import validate_catalog_text


class Tag(BaseSlug):
    """
    Модель тэга для товаров
    """

    manager = BaseManager()

    name = models.CharField(max_length=150, default=None)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(BaseSlug):
    """
    Модель категории товара
    """

    manager = CategoriesManager()

    name = models.CharField(max_length=150, default=None)

    weight = models.PositiveSmallIntegerField(
        default=100, help_text='Максимум 32767', verbose_name='Вес',

        # использую валидатор, т.к. в условии задачи > 0,
        # а PositiveSmallIntegerField => (0, 32767)
        # https://docs.djangoproject.com/en/4.0/ref/models/fields/#positivesmallintegerfield

        validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['weight', 'name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(Base):
    """
    Модель товара
    """

    manager = ItemsManager()

    name = models.CharField(
        max_length=150, verbose_name='Название',
        help_text='Максимум 150 символов'
    )

    text = models.TextField(
        validators=[validate_catalog_text],
        verbose_name='Описание',
        help_text='Минимум 2 слова, используйте "роскошно/превосходно"'
    )

    category = models.ForeignKey(
        Category, on_delete=models.RESTRICT, default=None,
        verbose_name='Категория', help_text='Категория товара'
    )

    tags = models.ManyToManyField(Tag, default=None, verbose_name='Тэги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

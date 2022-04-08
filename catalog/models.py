from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import QuerySet

from catalog.validators import validate_catalog_text
from core.models import Base, BaseSlug


class Tag(BaseSlug):
    """
    Модель тэга для товаров
    """

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

    name = models.CharField(max_length=150, default=None)

    weight = models.PositiveSmallIntegerField(
        default=100, help_text='Максимум 32767', verbose_name='Вес',

        # использую валидатор, т.к. в условии задачи > 0,
        # а PositiveSmallIntegerField => (0, 32767)
        # https://docs.djangoproject.com/en/4.0/ref/models/fields/#positivesmallintegerfield

        validators=[MinValueValidator(1)]
    )

    @staticmethod
    def get_all() -> QuerySet:
        return Category.objects.all()

    @staticmethod
    def filter(categories: QuerySet, **kwargs) -> QuerySet:
        return categories.filter(**kwargs)

    @staticmethod
    def join_items(categories: QuerySet, *fields) -> QuerySet:
        return categories.prefetch_related('item_set').only(*fields)

    @staticmethod
    def sorted(categories: QuerySet) -> list:
        return sorted(categories, key=lambda x: x.weight)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(Base):
    """
    Модель товара
    """

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

    @staticmethod
    def get_all() -> QuerySet:
        return Item.objects.all()

    @staticmethod
    def filter(items: QuerySet, **kwargs) -> QuerySet:
        return items.filter(**kwargs)

    @staticmethod
    def join_tags(items: QuerySet, *fields) -> QuerySet:
        return items.prefetch_related('tags').only(*fields)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

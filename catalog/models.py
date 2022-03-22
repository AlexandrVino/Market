from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from catalog.validators import validate_catalog_text
from core.models import Base, BaseSlug


class Tag(BaseSlug):
    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(BaseSlug):
    weight = models.IntegerField(default=100,
                                 validators=[MaxValueValidator(32767),
                                             MinValueValidator(1)])

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(Base):
    is_published = models.BooleanField(default=True)
    name = models.CharField(max_length=150)
    text = models.TextField(validators=[validate_catalog_text])

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,
                                 default=None)
    tags = models.ManyToManyField(Tag, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

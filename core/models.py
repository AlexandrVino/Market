from django.core.validators import validate_slug
from django.db import models


class Base(models.Model):
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано')

    class Meta:
        abstract = True


class BaseSlug(Base):
    slug = models.CharField(
        max_length=200, unique=True, validators=[validate_slug],
        help_text='Максимум 200 символов', verbose_name='Название')

    class Meta:
        abstract = True

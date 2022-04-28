from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class Base(models.Model):
    """
    Базовый абстрактный класс моделей
    """

    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        abstract = True


class BaseSlug(Base):
    """
    Базовый абстрактный класс моделей (вместе с полем слага)
    """

    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="Максимум 200 символов",
        verbose_name="Название",
    )

    class Meta:
        abstract = True


class DefaultGallery(models.Model):
    verbose_name = "Картинки"

    def __init__(self,  verbose_name=None, *args, **kwargs):
        if verbose_name:
            self.verbose_name = verbose_name
        super().__init__(*args, **kwargs)

    image = models.ImageField(
        upload_to="uploads/", null=True, blank=True, verbose_name=verbose_name
    )

    def get_image_x1280(self):
        return get_thumbnail(self.image, "1280", quality=51)

    def get_image_400x300(self):
        return get_thumbnail(self.image, "400x300", crop="center", quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50">')
        return "Нет изображения"

    image_tmb.short_description = "Превью"
    image_tmb.allow_tags = True

    def get_image_url(self):
        if self.image:
            return f"{self.image.url}"
        return "Нет изображения"

    class Meta:
        abstract = True

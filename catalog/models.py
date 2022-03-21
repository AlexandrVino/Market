from django.contrib.auth.models import User
from django.db import models
from catalog.validators import validate


class PublishedBasedModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(
        'Название Категории', max_length=150,
        help_text='максимум 150 символов')


class Tag(models.Model):
    name = models.CharField()


class Item(PublishedBasedModel):
    name = models.CharField(
        'Название', max_length=150, help_text='максимум 150 символов')
    text = models.TextField(
        'Описание', help_text='минимум 2 слова', validators=[validate])
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='items')

    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.text[:15]


class Extend(models.Model):
    item = models.OneToOneField(
        Item, on_delete=models.CASCADE, related_name='extend')


class Like(models.Model):
    item = models.ForeignKey(Item)
    user = models.ForeignKey(User)



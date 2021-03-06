# Generated by Django 3.2.12 on 2022-04-27 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.SmallIntegerField(blank=True, choices=[(1, 'Ненависть'), (2, 'Неприязнь'), (3, 'Нейтрально'), (4, 'Обожание'), (5, 'Любовь'), (0, 'Не могу сказать')], default=0, help_text='Поставьте рейтинг от 1 до 5')),
                ('item', models.ForeignKey(default=None, help_text='Пожалуйста, укажите товар', on_delete=django.db.models.deletion.CASCADE, to='catalog.item')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('user', 'item'), name='unique'),
        ),
    ]

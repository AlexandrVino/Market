# Generated by Django 3.2.12 on 2022-03-23 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0016_alter_rating_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.SmallIntegerField(choices=[('1', 'Ненависть'), ('2', 'Неприязнь'), ('3', 'Нейтрально'), ('4', 'Обожание'), ('5', 'Любовь'), ('0', 'Не могу сказать')], help_text='Поставьте рейтинг от 1 до 5'),
        ),
    ]
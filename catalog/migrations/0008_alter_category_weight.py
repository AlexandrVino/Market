# Generated by Django 3.2.12 on 2022-03-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20220323_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.PositiveSmallIntegerField(default=100, help_text='Максимум 32767', verbose_name='Вес'),
        ),
    ]
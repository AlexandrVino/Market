# Generated by Django 3.2.12 on 2022-03-21 08:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20220321_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Опубликовано ли ?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(help_text='Максимум 200 символов', max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')]),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.category'),
        ),
        migrations.RemoveField(
            model_name='item',
            name='tags',
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(default=None, to='catalog.Tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Опубликовано ли ?'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.CharField(help_text='Максимум 200 символов', max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')]),
        ),
    ]
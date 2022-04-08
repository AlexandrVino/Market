# Generated by Django 3.2.12 on 2022-03-21 06:21

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=150)),
                ('text', models.TextField(validators=[catalog.validators.validate_catalog_text])),
            ],
        ),
    ]
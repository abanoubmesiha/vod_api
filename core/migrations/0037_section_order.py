# Generated by Django 4.0.3 on 2022-06-23 12:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_rename_releaseyear_series_release_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.IntegerField(default=20, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)]),
        ),
    ]

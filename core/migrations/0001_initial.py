# Generated by Django 4.0.3 on 2022-06-02 12:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ar', models.CharField(max_length=150)),
                ('title_en', models.CharField(max_length=150)),
                ('description_ar', models.CharField(max_length=5000)),
                ('description_en', models.CharField(max_length=5000)),
                ('cover', models.CharField(blank=True, max_length=300, null=True)),
                ('poster', models.CharField(blank=True, max_length=300, null=True)),
                ('trailer', models.CharField(blank=True, max_length=300, null=True)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('releaseYear', models.IntegerField(default=1888, validators=[django.core.validators.MaxValueValidator(2999), django.core.validators.MinValueValidator(1888)])),
                ('duration', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5160), django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

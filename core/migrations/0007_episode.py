# Generated by Django 4.0.3 on 2022-06-02 12:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_series_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(728), django.core.validators.MinValueValidator(1)])),
                ('cover', models.CharField(blank=True, max_length=300, null=True)),
                ('series', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.series')),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-02 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.country'),
        ),
    ]

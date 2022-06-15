# Generated by Django 4.0.3 on 2022-06-15 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_alter_artist_id_alter_comment_id_alter_country_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, to='core.actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.director'),
        ),
        migrations.DeleteModel(
            name='Cast',
        ),
    ]

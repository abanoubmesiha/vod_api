# Generated by Django 4.0.3 on 2022-06-13 12:16

import core.models.movie
import core.models.series
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_artist_id_alter_comment_id_alter_country_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='video',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        # `upload_episode_to` is deleted from the model file and it throws errors
        # migrations.AlterField(
        #     model_name='episode',
        #     name='cover',
        #     field=models.ImageField(blank=True, default='default.gif', null=True, upload_to=core.models.series.upload_episode_to),
        # ),
        migrations.AlterField(
            model_name='movie',
            name='cover',
            field=models.ImageField(blank=True, default='default.gif', null=True, upload_to=core.models.movie.upload_to),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, default='default.gif', null=True, upload_to=core.models.movie.upload_to),
        ),
        migrations.AlterField(
            model_name='series',
            name='cover',
            field=models.ImageField(blank=True, default='default.gif', null=True, upload_to=core.models.series.upload_to),
        ),
        migrations.AlterField(
            model_name='series',
            name='poster',
            field=models.ImageField(blank=True, default='default.gif', null=True, upload_to=core.models.series.upload_to),
        ),
    ]

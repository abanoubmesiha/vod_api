# Generated by Django 4.0.3 on 2022-06-29 09:46

import core.models.series
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_episode_video_low_q_episode_video_medium_q_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='cover',
            field=models.ImageField(blank=True, default='logo2.png', null=True, upload_to=core.models.series.upload_episode_to),
        ),
    ]

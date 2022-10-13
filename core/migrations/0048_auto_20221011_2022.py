# Generated by Django 2.1.15 on 2022-10-11 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_episode_streaming_server'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='streaming_server',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='video',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='video_low_q',
        ),
        migrations.RemoveField(
            model_name='episode',
            name='video_medium_q',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='streaming_server',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='video',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='video_low_q',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='video_medium_q',
        ),
        migrations.AlterField(
            model_name='artist',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='country',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='section',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='series',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Streaming_Server',
        ),
    ]

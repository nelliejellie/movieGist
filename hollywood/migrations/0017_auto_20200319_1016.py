# Generated by Django 3.0.2 on 2020-03-19 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hollywood', '0016_auto_20200318_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gist',
            old_name='gist_dislike',
            new_name='movie_dislike',
        ),
        migrations.RenameField(
            model_name='gist',
            old_name='gist_like',
            new_name='movie_like',
        ),
        migrations.RenameField(
            model_name='tvshowgist',
            old_name='gist_dislike',
            new_name='tvshow_dislike',
        ),
        migrations.RenameField(
            model_name='tvshowgist',
            old_name='gist_like',
            new_name='tvshow_like',
        ),
    ]

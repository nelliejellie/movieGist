# Generated by Django 3.0.2 on 2020-03-15 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hollywood', '0008_remove_tvshowgist_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gist',
            name='tvshow',
        ),
    ]

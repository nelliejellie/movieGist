# Generated by Django 3.0.2 on 2020-02-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hollywood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movies',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.0.2 on 2020-03-15 04:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hollywood', '0006_gist_tvshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='tvshowgist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gists', models.TextField(max_length=300, null=True)),
                ('gist_like_counts', models.IntegerField(default=0)),
                ('gist_dislike_counts', models.IntegerField(default=0)),
                ('gist_like', models.BooleanField(default=False)),
                ('gist_dislike', models.BooleanField(default=False)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hollywood.Movies')),
                ('tvshow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hollywood.Tvshows')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

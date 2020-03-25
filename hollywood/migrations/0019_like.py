# Generated by Django 3.0.2 on 2020-03-19 20:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hollywood', '0018_auto_20200319_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('tvshow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mydislikes', to='hollywood.Tvshows')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mylikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

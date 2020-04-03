# Generated by Django 3.0.2 on 2020-03-29 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hollywood', '0023_auto_20200319_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hollywoodmoviesuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hollywoodtvshowuser', to=settings.AUTH_USER_MODEL),
        ),
    ]

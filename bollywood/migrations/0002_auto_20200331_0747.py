# Generated by Django 3.0.2 on 2020-03-31 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bollywood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bollywoodmoviesuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tvshows',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bollywoodtvshowuser', to=settings.AUTH_USER_MODEL),
        ),
    ]

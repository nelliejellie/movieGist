# Generated by Django 3.0.2 on 2020-03-18 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hollywood', '0012_auto_20200317_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gist',
            name='not_worth_seeing',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tvshowgist',
            name='not_worth_seeing',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
    ]

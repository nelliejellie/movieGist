# Generated by Django 3.0.2 on 2020-03-19 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hollywood', '0022_auto_20200319_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gist',
            name='not_worth_seeing',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gist',
            name='worth_seeing',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

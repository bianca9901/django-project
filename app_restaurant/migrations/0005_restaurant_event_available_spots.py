# Generated by Django 3.2.20 on 2023-08-09 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurant', '0004_auto_20230808_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant_event',
            name='available_spots',
            field=models.PositiveIntegerField(default=30),
        ),
    ]

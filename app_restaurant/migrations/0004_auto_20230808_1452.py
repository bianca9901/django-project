# Generated by Django 3.2.20 on 2023-08-08 14:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurant', '0003_auto_20230807_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant_reservation',
            name='solo',
        ),
        migrations.AlterField(
            model_name='restaurant_reservation',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='app_restaurant.restaurant_event'),
        ),
        migrations.AlterField(
            model_name='restaurant_reservation',
            name='num_friends',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30)]),
        ),
    ]

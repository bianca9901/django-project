# Generated by Django 3.2.20 on 2023-08-09 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurant', '0007_restaurant_event_available_spots'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant_event',
            name='employee',
        ),
    ]
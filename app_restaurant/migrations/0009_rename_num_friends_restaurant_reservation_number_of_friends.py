# Generated by Django 3.2.20 on 2023-08-10 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_restaurant', '0008_remove_restaurant_event_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant_reservation',
            old_name='num_friends',
            new_name='number_of_friends',
        ),
    ]

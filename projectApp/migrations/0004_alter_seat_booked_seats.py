# Generated by Django 4.0.3 on 2024-03-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0003_remove_bus_bus_destination_remove_bus_bus_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='booked_seats',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
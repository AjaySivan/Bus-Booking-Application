# Generated by Django 4.0.3 on 2024-03-21 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0009_boarddroppoints_stop_points'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boarddroppoints',
            old_name='stop_id',
            new_name='point_id',
        ),
        migrations.RemoveField(
            model_name='stop',
            name='points',
        ),
        migrations.AddField(
            model_name='boarddroppoints',
            name='stop',
            field=models.ManyToManyField(to='projectApp.stop'),
        ),
    ]

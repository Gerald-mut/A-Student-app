# Generated by Django 5.0.7 on 2024-09-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='end_time',
            field=models.TimeField(default='19:00'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='start_time',
            field=models.TimeField(default='7:30'),
        ),
    ]

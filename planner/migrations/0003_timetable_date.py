# Generated by Django 5.0.7 on 2024-09-24 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_timetable_end_time_timetable_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

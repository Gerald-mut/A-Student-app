from django.db import models
from django.conf import settings
from datetime import date
# Create your models here.
class Timetable(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ])
    start_time = models.TimeField(default='7:30')
    end_time = models.TimeField(default='19:00')
    date = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.subject} on {self.day_of_week} from {self.start_time} to {self.end_time}"
    

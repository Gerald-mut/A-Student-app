from django.contrib import admin
from .models import Timetable

# Register your models here.

class TimetableAdmin(admin.ModelAdmin):
    model = Timetable
    list_display = ('student', 'subject', 'day_of_week', 'start_time', 'end_time')
    fields = ('student', 'subject', 'day_of_week', 'start_time', 'end_time')

admin.site.register(Timetable, TimetableAdmin)
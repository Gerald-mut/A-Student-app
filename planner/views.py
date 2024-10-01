from django.shortcuts import render
from .models import Timetable
from datetime import date
import calendar

# Create your views here.
def timetable_view(request):
    student = request.user

    timetable = Timetable.objects.filter(student=student).order_by('day_of_week', 'start_time')

    return render(request, "planner/timetable.html", {
        'timetable': timetable
    })

def schedule_view(request):
    student = request.user
    subject = Timetable.objects.filter(student=student).values_list('subject', flat=True).distinct()
    subjectFromQuery = request.GET.get('subject')
    subject_entries = Timetable.objects.filter(student=student).order_by('day_of_week', 'start_time')
    if subjectFromQuery and subjectFromQuery != "":
        subject_entries = subject_entries.filter(subject_iexact=subjectFromQuery.strip())
    return render(request, "planner/schedule.html", {
        'subject_entries': subject_entries,
        'subject': subject
    })
    

def calendar_view(request):
    student = request.user
    subjects = Timetable.objects.filter(student=student).order_by('date')
    today = date.today()
    current_month = today.month
    current_year = today.year
    _, num_days = calendar.monthrange(current_year, current_month)
    days_in_month = range(1, num_days + 1)
    return render(request, "planner/calendar.html", {
        "subjects": subjects,
        "current_month": current_month,
        "current_year": current_year,
        "days_in_month": days_in_month,
    })
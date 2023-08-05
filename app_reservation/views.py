from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'John'
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)


    # Create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    #Get current year
    now = datetime.now()
    current_year = now.year
    # Get current time
    time = now.strftime('%H:%M %p')

    return render(request, 'app_reservation/home.html', {'name': name, 'year': year,
    'month': month, 'month_number': month_number, 'cal': cal, 'current_year': current_year, 'time': time, })
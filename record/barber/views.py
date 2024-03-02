from django.shortcuts import render
from calendarview.views import month_translation
import calendar
from .models import ScheduleBarber



def barber_count(request, month, num, year):
    
    num_month = '0' + str(month)
    month = f'{calendar.month_name[month]}'
    year = year
    month = month_translation(month)[1]
    barbers = ScheduleBarber.objects.filter(day=f'{year}-{num_month}-{num}')

    return render(request, 'barber.html', {'title': 'barber', 'num': num, 'month': month, 'year': year, 'barbers': barbers})
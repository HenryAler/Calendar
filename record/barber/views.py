from django.shortcuts import render
from calendarview.views import month_translation
import calendar
from .models import ScheduleBarber, Price, Barber



def barber_count(request, month, num, year):

    num_month = '0' + str(month)
    month = f'{calendar.month_name[month]}'
    month = month_translation(month)[1]
    barbers = ScheduleBarber.objects.filter(day=f'{year}-{num_month}-{num}')

    return render(request, 'barber.html', {'title': 'barber', 'num': num, 'month': month, 'year': year, 'barbers': barbers})


def price(request, **kwargs):
    if request.method == 'POST':
        barber = list(request.POST.keys())[0]
        barber_id = Barber.objects.filter(name=barber)
        for id in barber_id:
            price = Price.objects.filter(barber=id)
            
        return render(request, 'price.html', {'title': 'PriceList', 'price': price, 'barber': barber})
        
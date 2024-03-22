from django.shortcuts import render
from calendarview.views import month_translation
import calendar
from .models import ScheduleBarber, Price, Barber, WorkList
from django.shortcuts import redirect
from barber.forms import RecordForm



def barber_count(request, month, num, year):

    num_month = '0' + str(month)
    month = f'{calendar.month_name[month]}'
    month = month_translation(month)[1]
    try:
        barbers = ScheduleBarber.objects.get(day=f'{year}-{num_month}-{num}').barber.all()
        return render(request, 'barber.html', {'title': 'barber', 'num': num, 'month': month, 'year': year, 'barbers': barbers})
    except Exception as ex:
        return redirect('calendar')    


def price(request):

    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            WorkList.objects.create(
                name = data['name'],
                email = data['email'],
                time = data['time'],
                service = data['service'],
                barber = list(request.POST.items())[3][1]
            )
            return redirect('calendar')
        else:
            form = RecordForm()
            
        barber = list(request.POST.keys())[0]
        barber_id = Barber.objects.filter(name=barber)

        for id in barber_id:
            form.fields['service'].queryset = Price.objects.filter(barber=id)
            price = Price.objects.filter(barber=id)

        return render(request, 'price.html', {'title': 'PriceList', 'price': price, 'barber': barber, 'form': form})

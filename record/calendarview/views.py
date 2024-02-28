from django.shortcuts import render
import calendar
import time



def index(request):
    return render(request, 'index.html', {'title': 'home'})


def get_data(year, month):

    cal = calendar.Calendar(firstweekday=0)
    response = cal.monthdayscalendar(year, month)
    month_name = calendar.month_name[month]
    date = []
    for i in response:
        date.append(i)

    return month_name, date
    
def month_translation(month_name):

    """ Функция перводит названия месяцев на русский язык """

    dict_month = {'January': ('Январь', 'Января'),
                  'February': ('Февраль', 'Февраля'),
                  'March': ('Март', 'Марта'),
                  'April': ('Апрель', 'Апреля'),
                  'May': ('Май', 'Мая'),
                  'June': ('Июнь', 'Июня'),
                  'July': ('Июль', 'Июля'),
                  'August': ('Август', 'Августа'),
                  'September': ('Сентябрь', 'Сентября'),
                  'October': ('Октябрь', 'Октября'),
                  'November': ('Ноябрь', 'Ноября'),
                  'December': ('Декабрь', 'Декабря')
                  }
    
    return dict_month.get(month_name)

def view_calendar(request):

    if request.method == 'POST':
        
        month = int(list(request.POST.keys())[1]) + 1
        year = int(list(request.POST.values())[1])
        
        if month > 12:
            month = 1
            year += 1
        month_name, date = get_data(year, month)
        month_name = month_translation(month_name)[0]
        return render(request, 'calendar.html', {'date': date, 'month': month, 'title': 'calendar', 'year': year, 'month_name': month_name})
        
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    month_name, date = get_data(year, month)
    month_name = month_translation(month_name)[0]
    return render(request, 'calendar.html', {'date': date,  'month': month, 'title': 'calendar', 'year': year, 'month_name': month_name})
    



def barber_count(request, month, num):

    month = f'{calendar.month_name[month]}'
    month = month_translation(month)[1]
    

    return render(request, 'barber.html', {'title': 'barber', 'num': num, 'month': month})

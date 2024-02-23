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

    dict_month = {'January': 'Январь ',
                  'February': 'Февраль ',
                  'March': 'Март ',
                  'April': 'Апрель ',
                  'May': 'Май ',
                  'June': 'Июнь ',
                  'July': 'Июль ',
                  'August': 'Август ',
                  'September': 'Сентябрь ',
                  'October': 'Октябрь ',
                  'November': 'Ноябрь ',
                  'December': 'Декабрь '}
    
    return dict_month.get(month_name)

def view_calendar(request):

    if request.method == 'POST':
        
        month = int(list(request.POST.keys())[1]) + 1
        year = int(list(request.POST.values())[1])
        
        if month > 12:
            month = 1
            year += 1
        month_name, date = get_data(year, month)
        month_name = month_translation(month_name)
        return render(request, 'calendar.html', {'date': date, 'month': month, 'title': 'calendar', 'year': year, 'month_name': month_name})
        
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    month_name, date = get_data(year, month)
    month_name = month_translation(month_name)
    return render(request, 'calendar.html', {'date': date,  'month': month, 'title': 'calendar', 'year': year, 'month_name': month_name})
    



def barber_count(request, month, num):

    month = f'{calendar.month_name[month]}'
    month = month_translation(month)
    

    return render(request, 'barber.html', {'title': 'barber', 'num': num, 'month': month})







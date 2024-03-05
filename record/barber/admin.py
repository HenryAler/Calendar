from django.contrib import admin
from barber.models import Barber, ScheduleBarber, Price


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'getting_started', 'end_of_work']


@admin.register(ScheduleBarber)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['day', 'barber', 'working']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

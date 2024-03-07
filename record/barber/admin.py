from django.contrib import admin
from barber.models import Barber, ScheduleBarber, Price


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):

    list_display = ['name', 'surname', 'getting_started', 'end_of_work']
    list_filter = ['name']
    search_fields = ['name', 'surname']


@admin.register(ScheduleBarber)
class ScheduleAdmin(admin.ModelAdmin):

    list_display = ['day', 'barber', 'working']
    list_editable = ['barber']
    list_filter = ['day', 'barber']
    search_fields = ['barber']
    list_display_links = ['day']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'price']
    list_editable = ['name']
    list_filter = ['name']
    search_fields = ['name']
    list_display_links = ['price']
    
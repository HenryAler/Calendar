from django.contrib import admin
from barber.models import Barber, ScheduleBarber, Price


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):

    list_display = ['name', 'surname', 'getting_started', 'end_of_work']
    list_filter = ['name']
    search_fields = ['name', 'surname']


@admin.register(ScheduleBarber)
class ScheduleAdmin(admin.ModelAdmin):

    list_display = ['day', 'get_barber2','working']
    list_filter = ['day', 'barber']
    search_fields = ['barber']
    def get_barber2(self, obj):
        return [barber.name for barber in obj.barber.all()]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'price', 'durations', 'get_barber']
    list_filter = ['name']
    search_fields = ['name']
    def get_barber(self, obj):
        return [barber.name for barber in obj.barber.all()]
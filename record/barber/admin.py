from django.contrib import admin
from barber.models import Barber, ScheduleBarber, Price, WorkList


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):

    list_display = ['name', 'surname', 'getting_started', 'end_of_work']
    list_filter = ['name']
    search_fields = ['name', 'surname']


@admin.register(ScheduleBarber)
class ScheduleAdmin(admin.ModelAdmin):

    list_display = ['day', 'get_barber2']
    list_filter = ['day', 'barber']
    search_fields = ['barber']
    autocomplete_fields = ['barber']

    @admin.display(description='Работают')
    def get_barber2(self, obj):
        return [barber.name for barber in obj.barber.all()]


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'price', 'get_barber', 'durations']
    list_filter = ['name']
    search_fields = ['name']
    autocomplete_fields = ['barber']

    @admin.display(description='Мастера')
    def get_barber(self, obj):
        return [barber.name for barber in obj.barber.all()]
    

@admin.register(WorkList)
class WorkListAdmin(admin.ModelAdmin):
    list_display = ['name','time', 'service', 'barber', 'email']
    list_filter = ['barber', 'time']
from django.contrib import admin
from barber.models import Barber, Record

@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'fone', 'date', 'time', 'barber']
    

# admin.site.register(Barber)
# admin.site.register(Records)
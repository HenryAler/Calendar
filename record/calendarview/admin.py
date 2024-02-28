from django.contrib import admin
from calendarview.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'fone', 'date', 'time', 'barber']
    


# admin.site.register(Records)

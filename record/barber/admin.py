from django.contrib import admin
from barber.models import Barber


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']


# admin.site.register(Barber)
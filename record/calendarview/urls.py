from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.view_calendar, name='calendar'),
    path('barber/', views.barber_count, name='barber'),
    path('barber/<int:month>/<int:num>', views.barber_count, name='count'),
]
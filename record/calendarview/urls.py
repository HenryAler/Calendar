from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.view_calendar, name='calendar'),
    
]
from django.db import models
import datetime

class Barber(models.Model):

    name = models.CharField(max_length=15, verbose_name='Имя')
    surname = models.CharField(max_length=15, verbose_name='Фамилия')
    foto = models.ImageField(upload_to='Barber', verbose_name='Фото')
    getting_started = models.TimeField(null=True, default=datetime.time(9, 0, 0), verbose_name='Начало работы')
    end_of_work = models.TimeField(null=True, default=datetime.time(18, 0, 0), verbose_name='Окончание работы')

    def __str__(self):

        return self.name
    
    class Meta():

        ordering = ['name']
        verbose_name_plural = 'Мастера'
        

class ScheduleBarber(models.Model):

    day = models.DateField(null=True, verbose_name='День')
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, verbose_name='Мастер')
    working = models.BooleanField(default=False, verbose_name='Работает да/нет')

    def __str__(self):

        return 'Расписание работы мастеров'
    
    class Meta():

        ordering = ['day']
        verbose_name_plural = 'Расписание'


class Price(models.Model):

    name = models.TextField(max_length=100)
    price = models.FloatField()
    durations = models.DurationField()
    barber = models.ManyToManyField(Barber)

    def __str__(self):

        return 'Услуга'
    
    class Meta():
        ordering = ['name']
        verbose_name_plural = 'Услуги'
    
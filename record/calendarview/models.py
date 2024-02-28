from django.db import models
from barber.models import Barber


class Record(models.Model):

    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    fone = models.IntegerField()
    email = models.EmailField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

    class Meta():
        ordering = ['name']

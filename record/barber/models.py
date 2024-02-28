from django.db import models

class Barber(models.Model):

    name = models.CharField(max_length=15, verbose_name='Имя')
    surname = models.CharField(max_length=15, verbose_name='Фамилия')
    foto = models.ImageField(upload_to='Barber')

    def __str__(self):
        # return f'{self.name} {self.surname}'
        return self.name
    
    class Meta():
        ordering = ['name']
        
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

class Client(models.Model):
    pass


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

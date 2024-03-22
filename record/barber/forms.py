from django import forms
from .models import Barber, Price


class RecordForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    time = forms.TimeField(label='Время')
    service = forms.ModelChoiceField(label='Услуга', queryset=None, empty_label='Выберите услугу')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["service"].queryset = Price.objects.all()

from django import forms
from .models import Barber, Price


class RecordForm(forms.Form):

    time = forms.TimeField(label='Время')
    service = forms.ModelChoiceField(label='Услуга', queryset=None, empty_label='Услуга')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["service"].queryset = Price.objects.all()

from django import forms
from django.forms.extras import widgets
from .models import Appointment, TimeManager


class AppointmentForm(forms.ModelForm):
    day = forms.DateField(widget=widgets.SelectDateWidget(years=TimeManager.year_))
    time = forms.TimeField(widget=widgets.Select(choices=[(' ', '------')]))

    class Meta:
        model = Appointment
        fields = ['doctor', 'day', 'time', 'patient']
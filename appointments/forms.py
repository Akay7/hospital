from datetime import datetime
from django.utils import timezone
from django import forms
from django.forms.extras import widgets
from .models import Doctor, Appointments

time_ = [(i, "%s:00" % i) for i in range(9, 18)]
year_ = [str(timezone.now().year)]


class AppointmentsForm(forms.ModelForm):
    day = forms.DateField(widget=widgets.SelectDateWidget(years=year_))
    time = forms.TimeField(widget=widgets.Select(choices=time_))

    class Meta:
        model = Appointments
        fields = ['doctor', 'day', 'time', 'patient']
from django.views import generic
from .forms import AppointmentsForm


class AppointmentsFormView(generic.FormView):
    form_class = AppointmentsForm
    template_name = 'appointments/appointments.html'
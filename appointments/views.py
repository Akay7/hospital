from django.views import generic
from django.http import JsonResponse
from django.core.urlresolvers import reverse_lazy
from .forms import AppointmentForm
from .models import TimeManager


class AppointmentsFormView(generic.FormView):
    form_class = AppointmentForm
    success_url = reverse_lazy('appointments:registration')
    template_name = 'appointments/appointments.html'

    def form_valid(self, form):
        form.save()
        return super(AppointmentsFormView, self).form_valid(form)


class GetFreeTimeView(generic.View):
    def post(self, request):
        doctor_id = request.POST.get("doctor_id")
        day = request.POST.get('day')
        #print(day)
        answer = dict(TimeManager.get_free_time(doctor_id, day))

        return JsonResponse(answer)
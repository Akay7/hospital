from datetime import date
from django.utils import timezone
from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor)
    day = models.DateField()
    time = models.TimeField()
    patient = models.CharField(max_length=200)

    class Meta:
        unique_together = [
            ('doctor', 'day', 'time',),
        ]


class TimeManager:
    time_ = set([("%s:00:00" % i, "%s:00" % i) for i in range(9, 18)])
    year_ = [str(timezone.now().year)]

    @staticmethod
    def get_free_time(doctor_id, day):
        doctor = Doctor.objects.get(id=doctor_id)
        not_free_set = set([(str(appointment.time), str(appointment.time)[:-3])
                            for appointment in doctor.appointment_set.all()
                            if date(*list(map(int, day.split('-')))) == appointment.day])

        return TimeManager.time_ - not_free_set
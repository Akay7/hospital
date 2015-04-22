from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Appointments(models.Model):
    doctor = models.ForeignKey(Doctor)
    day = models.DateField()
    time = models.TimeField()
    patient = models.CharField(max_length=200)


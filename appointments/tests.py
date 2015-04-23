from django.test import TestCase
from .models import Appointment, Doctor, TimeManager
from .forms import AppointmentForm


class TestFormAppointment(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(name="Gordon Freeman")
        self.doctor2 = Doctor.objects.create(name="Isaac Kleiner")

    def test_add_new_appointment(self):
        data = {'doctor': self.doctor.id, 'day': '2015-04-23', 'time': '10:00:00', 'patient': 'Head Crab'}
        form = AppointmentForm(data)
        self.assertEqual(form.is_valid(), True)

    def test_cant_add_multiply_appointments_to_one_doctor(self):
        data = {'doctor': self.doctor.id, 'day': '2015-04-23', 'time': '10:00:00', 'patient': 'Head Crab'}
        form = AppointmentForm(data)
        form.save()
        form2 = AppointmentForm(data)
        self.assertEqual(form2.is_valid(), False)

    def test_can_add_at_same_time_appointments_to_different_doctors(self):
        data = {'doctor': self.doctor.id, 'day': '2015-04-23', 'time': '10:00:00', 'patient': 'Head Crab'}
        form = AppointmentForm(data)
        form.save()
        data2 = {'doctor': self.doctor2.id, 'day': '2015-04-23', 'time': '10:00:00', 'patient': 'Lamar'}
        form2 = AppointmentForm(data2)
        self.assertEqual(form2.is_valid(), True)


class TestGetFreeTime(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(name="Gordon Freeman")
        self.doctor2 = Doctor.objects.create(name="Isaac Kleiner")
        Appointment.objects.create(doctor=self.doctor, day="2015-10-11", time="10:00:00", patient="Lamar")
        self.doctor.save()

    def test_returning_all_free_time_for_selected_day(self):
        response = self.client.post('/1/get_free_time', {"day": "2015-10-11", "doctor_id": self.doctor.id})
        self.assertNotIn(b'"10:00:00": "10:00"', response.content)
        self.assertIn(b'"11:00:00": "11:00"', response.content)

    def test_timemanager_returning_only_free_time(self):
        free_time = TimeManager.get_free_time(self.doctor.id, "2015-10-11")

        self.assertIn(("11:00:00", "11:00"), free_time)

        self.assertNotIn(("10:00:00", "10:00"), free_time)


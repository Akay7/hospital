from django.contrib import admin
from .models import Appointment, Doctor


class AppointmentAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Appointment, AppointmentAdmin)


class AppointmentStackedAdmin(admin.StackedInline):
    model = Appointment
    fields = ['day', 'time', 'patient', ]
    #readonly_fields = ['day', 'time', 'patient', ]
    extra = 0


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ('name', )
    inlines = [
        AppointmentStackedAdmin
    ]


admin.site.register(Doctor, DoctorAdmin)
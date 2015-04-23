# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20150422_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('day', models.DateField()),
                ('time', models.TimeField()),
                ('patient', models.CharField(max_length=200)),
                ('doctor', models.ForeignKey(to='appointments.Doctor')),
            ],
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Appointments',
        ),
    ]

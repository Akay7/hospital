# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_auto_20150423_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(choices=[('9:00:00', '9:00'), ('10:00:00', '10:00'), ('11:00:00', '11:00'), ('12:00:00', '12:00'), ('13:00:00', '13:00'), ('14:00:00', '14:00'), ('15:00:00', '15:00'), ('16:00:00', '16:00'), ('17:00:00', '17:00')]),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together=set([('doctor', 'day', 'time')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20150422_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='day',
            field=models.DateField(default=datetime.datetime(2015, 4, 22, 20, 15, 23, 648599, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointments',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

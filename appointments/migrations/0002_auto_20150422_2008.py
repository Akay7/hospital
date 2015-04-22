# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='patient',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0002_auto_20150531_1339'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OptionsEstimate',
            new_name='EstimatePrestaViticoles',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activities',
            old_name='price_ha_gd',
            new_name='unit_price_with_tax',
        ),
        migrations.RemoveField(
            model_name='activities',
            name='price_ha_gs',
        ),
        migrations.RemoveField(
            model_name='activities',
            name='price_plant_gd',
        ),
        migrations.RemoveField(
            model_name='activities',
            name='price_plant_gs',
        ),
    ]

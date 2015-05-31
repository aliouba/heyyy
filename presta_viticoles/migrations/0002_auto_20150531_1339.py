# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presta_viticoles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionsEstimate',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nb', models.FloatField(blank=True, null=True)),
                ('surface', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('type_guyot', models.CharField(blank=True, null=True, max_length=2)),
                ('largeur_entre_rangs', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('distance_entre_ceps', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('plant_superficie', models.CharField(blank=True, null=True, max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='distance_entre_ceps',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='largeur_entre_rangs',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='plant_superficie',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='surface',
        ),
        migrations.RemoveField(
            model_name='estimate',
            name='type_guyot',
        ),
        migrations.AddField(
            model_name='optionsestimate',
            name='estimate',
            field=models.ForeignKey(to='presta_viticoles.Estimate'),
        ),
    ]

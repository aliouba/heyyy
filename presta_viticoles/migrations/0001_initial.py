# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPrestaViticole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('price_plant_gd', models.DecimalField(max_digits=10, decimal_places=3, null=True)),
                ('price_plant_gs', models.DecimalField(max_digits=10, decimal_places=3, null=True)),
                ('price_ha_gs', models.DecimalField(max_digits=10, decimal_places=3, null=True)),
                ('price_ha_gd', models.DecimalField(max_digits=10, decimal_places=3, null=True)),
                ('tax', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=0, default=0)),
                ('creationdate', models.DateTimeField(null=True, auto_now_add=True)),
                ('modificationdate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('unit_price', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=3)),
                ('unit_type', models.CharField(blank=True, max_length=45)),
                ('price_with_tax', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=3)),
                ('price_without_tax', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=0)),
                ('tax', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=0)),
                ('creationdate', models.DateTimeField(null=True, auto_now_add=True)),
                ('modificationdate', models.DateTimeField(blank=True, null=True)),
                ('activity', models.ForeignKey(to='presta_viticoles.ActivityPrestaViticole')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=45, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('siret', models.CharField(blank=True, max_length=14, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=45, null=True)),
                ('mail', models.CharField(blank=True, max_length=45, null=True)),
                ('cp', models.CharField(blank=True, max_length=45, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('adresse', models.CharField(blank=True, max_length=45, null=True)),
                ('country', models.CharField(blank=True, max_length=45, null=True)),
                ('logo', models.FileField(blank=True, max_length=45, null=True, upload_to='')),
                ('creationdate', models.DateTimeField(null=True, auto_now_add=True)),
                ('modificationdate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigPrestaViticole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('guyots', models.BooleanField(default=False)),
                ('guyotd', models.BooleanField(default=False)),
                ('superficie', models.BooleanField(default=False)),
                ('plant', models.BooleanField(default=False)),
                ('nb_plants_min', models.IntegerField(default=0)),
                ('creationdate', models.DateTimeField(null=True, auto_now_add=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('company', models.ForeignKey(to='presta_viticoles.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('firstname', models.CharField(blank=True, max_length=45, null=True)),
                ('lastname', models.CharField(blank=True, max_length=45, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=45, null=True)),
                ('mail', models.CharField(max_length=255)),
                ('cp', models.CharField(blank=True, max_length=45, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('adresse', models.CharField(blank=True, max_length=45, null=True)),
                ('country', models.CharField(blank=True, max_length=45, null=True)),
                ('creationdate', models.DateTimeField(null=True, auto_now_add=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('firstname', models.CharField(max_length=45, null=True)),
                ('lastname', models.CharField(max_length=45, null=True)),
                ('phonenumber', models.CharField(max_length=45, null=True)),
                ('mail', models.CharField(max_length=45, null=True)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('company', models.ForeignKey(to='presta_viticoles.Company')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('creationdate', models.DateTimeField(null=True, auto_now_add=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('company_name', models.CharField(max_length=45, null=True)),
                ('nb', models.FloatField(blank=True, null=True)),
                ('price_with_tax', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=3)),
                ('price_without_tax', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=0)),
                ('type_guyot', models.CharField(blank=True, max_length=2, null=True)),
                ('largeur_entre_rangs', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=3)),
                ('distance_entre_ceps', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=3)),
                ('surface', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=3)),
                ('plant_superficie', models.CharField(blank=True, max_length=3, null=True)),
                ('customer', models.ForeignKey(to='presta_viticoles.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='benefit',
            name='estimate',
            field=models.ForeignKey(related_query_name='estimate', related_name='estimates', to='presta_viticoles.Estimate'),
        ),
        migrations.AddField(
            model_name='activityprestaviticole',
            name='company',
            field=models.ForeignKey(to='presta_viticoles.Company'),
        ),
        migrations.AddField(
            model_name='activityprestaviticole',
            name='group',
            field=models.ForeignKey(related_query_name='activity', related_name='activities', to='presta_viticoles.ActivityGroup'),
        ),
    ]

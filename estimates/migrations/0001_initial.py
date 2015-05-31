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
            name='Activities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(null=True, max_length=255)),
                ('description', models.CharField(null=True, max_length=255)),
                ('price_plant_gd', models.DecimalField(max_digits=10, null=True, decimal_places=3)),
                ('price_plant_gs', models.DecimalField(max_digits=10, null=True, decimal_places=3)),
                ('price_ha_gs', models.DecimalField(max_digits=10, null=True, decimal_places=3)),
                ('price_ha_gd', models.DecimalField(max_digits=10, null=True, decimal_places=3)),
                ('tax', models.DecimalField(blank=True, max_digits=10, decimal_places=0, null=True, default=0)),
                ('creationdate', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(null=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(null=True, max_length=255)),
                ('description', models.CharField(null=True, max_length=255)),
                ('unit_price', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=3)),
                ('unit_type', models.CharField(blank=True, max_length=45)),
                ('price_with_tax', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=3)),
                ('price_without_tax', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=3)),
                ('tax', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=0)),
                ('creationdate', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificationdate', models.DateTimeField(blank=True, null=True)),
                ('activity', models.ForeignKey(to='estimates.Activities')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(null=True, max_length=45)),
                ('description', models.CharField(blank=True, null=True, max_length=255)),
                ('siret', models.CharField(blank=True, null=True, max_length=14)),
                ('phonenumber', models.CharField(blank=True, null=True, max_length=45)),
                ('mail', models.CharField(blank=True, null=True, max_length=45)),
                ('cp', models.CharField(blank=True, null=True, max_length=45)),
                ('city', models.CharField(blank=True, null=True, max_length=45)),
                ('adresse', models.CharField(blank=True, null=True, max_length=45)),
                ('country', models.CharField(blank=True, null=True, max_length=45)),
                ('logo', models.FileField(blank=True, upload_to='', null=True, max_length=45)),
                ('creationdate', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('firstname', models.CharField(blank=True, null=True, max_length=45)),
                ('lastname', models.CharField(blank=True, null=True, max_length=45)),
                ('phonenumber', models.CharField(blank=True, null=True, max_length=45)),
                ('mail', models.CharField(max_length=255)),
                ('cp', models.CharField(blank=True, null=True, max_length=45)),
                ('city', models.CharField(blank=True, null=True, max_length=45)),
                ('adresse', models.CharField(blank=True, null=True, max_length=45)),
                ('country', models.CharField(blank=True, null=True, max_length=45)),
                ('creationdate', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('firstname', models.CharField(null=True, max_length=45)),
                ('lastname', models.CharField(null=True, max_length=45)),
                ('phonenumber', models.CharField(null=True, max_length=45)),
                ('mail', models.CharField(null=True, max_length=45)),
                ('creationdate', models.DateTimeField(null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('company', models.ForeignKey(to='estimates.Company')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('creationdate', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificationdate', models.DateTimeField(null=True)),
                ('company_name', models.CharField(null=True, max_length=45)),
                ('nb', models.FloatField(blank=True, null=True)),
                ('price_with_tax', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=3)),
                ('price_without_tax', models.DecimalField(blank=True, max_digits=10, null=True, decimal_places=3)),
                ('customer', models.ForeignKey(to='estimates.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='benefit',
            name='estimate',
            field=models.ForeignKey(related_name='estimates', to='estimates.Estimate', related_query_name='estimate'),
        ),
        migrations.AddField(
            model_name='activities',
            name='company',
            field=models.ForeignKey(to='estimates.Company'),
        ),
        migrations.AddField(
            model_name='activities',
            name='group',
            field=models.ForeignKey(related_name='activities', to='estimates.ActivityGroup', related_query_name='activity'),
        ),
    ]

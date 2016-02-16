# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 19:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
        ('stock', '0001_initial'),
        ('plate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('sample_date', models.DateField(null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('dbh', models.FloatField(blank=True, null=True)),
                ('angle_low', models.FloatField(blank=True, null=True)),
                ('angle_high', models.FloatField(blank=True, null=True)),
                ('angle_distance', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('bark1', models.FloatField(blank=True, null=True)),
                ('bark2', models.FloatField(blank=True, null=True)),
                ('bark3', models.FloatField(blank=True, null=True)),
                ('bark4', models.FloatField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('usable', models.BooleanField(default=True)),
                ('library_cell', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.LibraryCell')),
                ('plate_cell', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plate.PlateCell')),
                ('population', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='envdata.Population')),
                ('stock_cell', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.StockCell')),
            ],
        ),
    ]

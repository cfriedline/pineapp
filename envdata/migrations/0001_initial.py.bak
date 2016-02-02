# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('sample_date', models.DateField(null=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('dbh', models.FloatField(null=True, blank=True)),
                ('angle_low', models.FloatField(null=True, blank=True)),
                ('angle_high', models.FloatField(null=True, blank=True)),
                ('angle_distance', models.FloatField(null=True, blank=True)),
                ('height', models.FloatField(null=True, blank=True)),
                ('bark1', models.FloatField(null=True, blank=True)),
                ('bark2', models.FloatField(null=True, blank=True)),
                ('bark3', models.FloatField(null=True, blank=True)),
                ('bark4', models.FloatField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('freezer_box', models.IntegerField(null=True, blank=True)),
                ('freezer_box_row', models.CharField(null=True, blank=True, max_length=1)),
                ('freezer_box_col', models.IntegerField(null=True, blank=True)),
                ('population', models.ForeignKey(blank=True, to='envdata.Population', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

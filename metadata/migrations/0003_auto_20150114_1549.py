# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0002_sample_sample_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='angle_distance',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='angle_high',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='angle_low',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='bark1',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='bark2',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='bark3',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='bark4',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='dbh',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='height',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='lat',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='lon',
            field=models.FloatField(blank=True),
            preserve_default=True,
        ),
    ]

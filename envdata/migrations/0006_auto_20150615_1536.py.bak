# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plate', '__first__'),
        ('envdata', '0005_sample_barcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='barcode',
        ),
        migrations.AddField(
            model_name='sample',
            name='plate',
            field=models.ForeignKey(blank=True, to='plate.PlateCell', null=True),
            preserve_default=True,
        ),
    ]

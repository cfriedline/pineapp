# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '__first__'),
        ('envdata', '0004_sample_freezer'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='barcode',
            field=models.ForeignKey(blank=True, to='barcode.Barcode', null=True),
            preserve_default=True,
        ),
    ]

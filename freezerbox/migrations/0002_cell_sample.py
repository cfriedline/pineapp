# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envdata', '0002_auto_20150615_1343'),
        ('freezerbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='sample',
            field=models.ForeignKey(blank=True, to='envdata.Sample', null=True),
            preserve_default=True,
        ),
    ]

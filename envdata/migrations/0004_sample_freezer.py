# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freezerbox', '0003_auto_20150615_1438'),
        ('envdata', '0003_auto_20150615_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='freezer',
            field=models.ForeignKey(blank=True, to='freezerbox.FreezerBoxCell', null=True),
            preserve_default=True,
        ),
    ]

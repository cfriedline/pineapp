# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freezerbox', '0003_auto_20150615_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='freezerbox',
            name='kind',
            field=models.CharField(default=b'STK', max_length=3, choices=[(b'STK', b'Stock'), (b'LIB', b'Library')]),
        ),
    ]

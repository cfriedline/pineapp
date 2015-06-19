# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freezerbox', '0005_auto_20150619_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freezerboxcell',
            name='row',
            field=models.CharField(max_length=2),
        ),
    ]

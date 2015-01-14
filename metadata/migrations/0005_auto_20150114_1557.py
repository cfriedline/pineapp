# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0004_auto_20150114_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='name',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
    ]

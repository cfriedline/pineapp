# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envdata', '0012_auto_20151124_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='library_cell',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='stock_cell',
        ),
    ]

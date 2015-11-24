# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envdata', '0013_auto_20151124_1819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='library_cell2',
            new_name='library_cell',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='stock_cell2',
            new_name='stock_cell',
        ),
    ]

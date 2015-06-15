# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envdata', '0006_auto_20150615_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='freezer',
            new_name='freezer_cell',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='plate',
            new_name='plate_cell',
        ),
    ]

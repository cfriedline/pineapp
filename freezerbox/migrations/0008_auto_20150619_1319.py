# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freezerbox', '0007_auto_20150619_1311'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='freezerboxcell',
            unique_together=set([('box', 'row', 'col')]),
        ),
    ]

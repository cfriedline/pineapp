# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    # dependencies = [
    #     ('freezerbox', '0004_freezerbox_kind'),
    #     ('envdata', '0007_auto_20150615_1612'),
    # ]
    #
    dependencies = [
        ('envdata', '0007_auto_20150615_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='freezer_cell',
        ),
        migrations.AddField(
            model_name='sample',
            name='library_cell',
            field=models.ForeignKey(related_name='library', blank=True, to='freezerbox.FreezerBoxCell', null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='stock_cell',
            field=models.ForeignKey(related_name='stock', blank=True, to='freezerbox.FreezerBoxCell', null=True),
        ),
    ]

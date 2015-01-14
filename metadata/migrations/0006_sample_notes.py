# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0005_auto_20150114_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='notes',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

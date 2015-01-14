# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='sample_date',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
    ]

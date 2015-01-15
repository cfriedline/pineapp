# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0007_population'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='population',
            field=models.ForeignKey(blank=True, to='metadata.Population', null=True),
            preserve_default=True,
        ),
    ]

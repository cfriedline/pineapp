# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freezerbox', '0004_freezerbox_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freezerbox',
            name='name',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plate', '0003_auto_20150615_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='platecell',
            name='plate',
            field=models.ForeignKey(blank=True, null=True, to='plate.Plate'),
        ),
        migrations.AlterUniqueTogether(
            name='platecell',
            unique_together=set([('plate', 'row', 'col')]),
        ),
    ]

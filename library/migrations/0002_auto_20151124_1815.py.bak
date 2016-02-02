# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='librarycell',
            old_name='stock',
            new_name='box',
        ),
        migrations.AlterUniqueTogether(
            name='librarycell',
            unique_together=set([('box', 'row', 'col')]),
        ),
    ]

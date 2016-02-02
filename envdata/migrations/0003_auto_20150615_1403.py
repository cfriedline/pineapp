# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envdata', '0002_auto_20150615_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='freezer_box',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='freezer_box_col',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='freezer_box_row',
        ),
    ]

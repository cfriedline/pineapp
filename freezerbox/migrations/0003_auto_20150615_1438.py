# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freezerbox', '0002_cell_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreezerBoxCell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row', models.CharField(max_length=1)),
                ('col', models.IntegerField()),
                ('box', models.ForeignKey(to='freezerbox.FreezerBox')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cell',
            name='box',
        ),
        migrations.RemoveField(
            model_name='cell',
            name='sample',
        ),
        migrations.DeleteModel(
            name='Cell',
        ),
    ]

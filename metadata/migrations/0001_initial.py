# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('name', models.CharField(max_length=20)),
                ('dbh', models.FloatField()),
                ('angle_low', models.FloatField()),
                ('angle_high', models.FloatField()),
                ('angle_distance', models.FloatField()),
                ('height', models.FloatField()),
                ('bark1', models.FloatField()),
                ('bark2', models.FloatField()),
                ('bark3', models.FloatField()),
                ('bark4', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

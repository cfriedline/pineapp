# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlateCell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row', models.CharField(max_length=1)),
                ('col', models.IntegerField()),
                ('barcode', models.ForeignKey(blank=True, to='barcode.Barcode', null=True)),
                ('plate', models.ForeignKey(to='plate.Plate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

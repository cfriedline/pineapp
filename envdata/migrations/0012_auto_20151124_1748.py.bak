# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
        ('library', '0001_initial'),
        ('envdata', '0011_auto_20151124_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='library_cell2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='library.LibraryCell', null=True),
        ),
        migrations.AddField(
            model_name='sample',
            name='stock_cell2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='stock.StockCell', null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='library_cell',
            field=models.ForeignKey(related_name='library', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='freezerbox.FreezerBoxCell', null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='stock_cell',
            field=models.ForeignKey(related_name='stock', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='freezerbox.FreezerBoxCell', null=True),
        ),
    ]

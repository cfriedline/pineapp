# -*- coding: utf-8 -*-


from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('envdata', '0008_auto_20150619_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='library_cell',
            field=models.ForeignKey(related_name='library', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='freezerbox.FreezerBoxCell', null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='plate_cell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='plate.PlateCell', null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='stock_cell',
            field=models.ForeignKey(related_name='stock', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='freezerbox.FreezerBoxCell', null=True),
        ),
    ]

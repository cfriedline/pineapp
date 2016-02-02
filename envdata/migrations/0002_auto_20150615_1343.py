# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='freezer_box',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sample',
            name='freezer_box_row',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

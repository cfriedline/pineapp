# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('envdata', '0009_auto_20150619_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='usable',
            field=models.BooleanField(default=True),
        ),
    ]

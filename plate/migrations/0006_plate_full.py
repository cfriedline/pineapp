# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plate', '0005_auto_20150619_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='full',
            field=models.BooleanField(default=False),
        ),
    ]

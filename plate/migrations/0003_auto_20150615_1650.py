# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plate', '0002_remove_platecell_plate'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='platecell',
            unique_together=set([('row', 'col')]),
        ),
    ]

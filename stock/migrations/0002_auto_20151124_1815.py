# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockcell',
            old_name='stock',
            new_name='box',
        ),
        migrations.AlterUniqueTogether(
            name='stockcell',
            unique_together=set([('box', 'row', 'col')]),
        ),
    ]

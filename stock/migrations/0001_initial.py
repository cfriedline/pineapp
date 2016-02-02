# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('full', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StockCell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('row', models.CharField(max_length=1)),
                ('col', models.IntegerField()),
                ('stock', models.ForeignKey(blank=True, to='stock.Stock', null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='stockcell',
            unique_together=set([('stock', 'row', 'col')]),
        ),
    ]

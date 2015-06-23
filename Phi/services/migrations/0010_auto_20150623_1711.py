# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_auto_20150623_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='avg_rate',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='total_raters',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]

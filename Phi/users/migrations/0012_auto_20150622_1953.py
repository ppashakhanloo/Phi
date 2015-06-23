# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20150622_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='followees',
            field=models.ManyToManyField(blank=True, to='users.Member'),
        ),
    ]

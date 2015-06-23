# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20150622_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='followees',
            field=models.ManyToManyField(null=True, to='users.Member'),
        ),
    ]

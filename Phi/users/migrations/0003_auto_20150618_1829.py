# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150530_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='followees',
            field=models.ManyToManyField(to='users.Member', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150618_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='followees',
            field=models.ManyToManyField(null=True, to='users.Member'),
        ),
    ]

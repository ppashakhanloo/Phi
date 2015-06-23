# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150530_1556'),
        ('services', '0002_auto_20150616_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likers',
        ),
        migrations.AddField(
            model_name='post',
            name='likers',
            field=models.ManyToManyField(to='users.Member', related_name='liker', null=True),
        ),
    ]

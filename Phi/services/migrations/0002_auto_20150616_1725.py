# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150530_1556'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likers',
        ),
        migrations.AddField(
            model_name='post',
            name='likers',
            field=models.ForeignKey(to='users.Member', null=True, related_name='liker'),
        ),
    ]

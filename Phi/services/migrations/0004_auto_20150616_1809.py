# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150530_1556'),
        ('services', '0003_auto_20150616_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('member', models.ForeignKey(to='users.Member')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='likers',
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(to='services.Post'),
        ),
    ]

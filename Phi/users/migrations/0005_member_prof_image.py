# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150618_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='prof_image',
            field=models.ImageField(null=True, verbose_name='Profile Pic', upload_to='images/', blank='True'),
        ),
    ]

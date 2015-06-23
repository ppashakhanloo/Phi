# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20150622_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='prof_image',
            field=models.ImageField(blank='True', upload_to='media/', default='media/unknown.png'),
        ),
    ]

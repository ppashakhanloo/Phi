# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150622_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='prof_image',
            field=models.ImageField(upload_to='media/', null=True, blank='True', default='media/unknown.png'),
        ),
    ]

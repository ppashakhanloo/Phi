# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150622_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='prof_image',
            field=models.ImageField(null=True, upload_to='/', blank='True'),
        ),
    ]

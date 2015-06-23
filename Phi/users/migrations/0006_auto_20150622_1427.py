# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_member_prof_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='prof_image',
            field=models.FileField(null=True, upload_to='images/prof/', blank='True'),
        ),
    ]

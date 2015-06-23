# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20150622_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_image',
            field=models.ImageField(upload_to='media/', null=True, blank='True', default='media/unknown-movie.png'),
        ),
    ]

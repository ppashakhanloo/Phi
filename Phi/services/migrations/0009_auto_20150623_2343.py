# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_movie_poster_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='avg_rate',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='total_raters',
        ),
        migrations.AddField(
            model_name='actor',
            name='actor_image',
            field=models.ImageField(blank='True', null=True, upload_to='media/'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150530_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('comment_text', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('member', models.ForeignKey(to='users.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('year', models.PositiveSmallIntegerField()),
                ('avg_rate', models.FloatField()),
                ('link_to_imdb', models.CharField(max_length=300)),
                ('total_raters', models.PositiveIntegerField()),
                ('summary', models.TextField()),
                ('genre', models.CharField(max_length=40)),
                ('initial_release', models.DateField()),
                ('director', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=40)),
                ('author', models.CharField(max_length=100)),
                ('song_writer', models.CharField(max_length=100)),
                ('cinematography', models.CharField(max_length=100)),
                ('running_time', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('notif_type', models.CharField(max_length=20)),
                ('seen', models.BooleanField(default='false')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('rate', models.PositiveSmallIntegerField()),
                ('post_text', models.TextField(max_length=500)),
                ('datetime', models.DateTimeField()),
                ('likers', models.ManyToManyField(null=True, to='users.Member', related_name='liker')),
                ('member', models.ForeignKey(to='users.Member', related_name='author')),
                ('movie', models.ForeignKey(to='services.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('role_name', models.CharField(max_length=50)),
                ('actor', models.ForeignKey(to='services.Actor')),
                ('movie', models.ForeignKey(to='services.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='PostRelatedNotif',
            fields=[
                ('notification_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, primary_key=True, to='services.Notification')),
                ('post', models.ForeignKey(to='services.Post')),
            ],
            bases=('services.notification',),
        ),
        migrations.AddField(
            model_name='notification',
            name='notif_object',
            field=models.ForeignKey(to='users.Member', related_name='object'),
        ),
        migrations.AddField(
            model_name='notification',
            name='notif_subject',
            field=models.ForeignKey(to='users.Member', related_name='subject'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, to='services.Post'),
        ),
    ]

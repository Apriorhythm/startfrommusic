# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfm_music', '0002_uploadfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='netease',
            name='uploadId',
        ),
        migrations.AddField(
            model_name='netease',
            name='uploadDate',
            field=models.DateField(auto_now=True),
        ),
    ]

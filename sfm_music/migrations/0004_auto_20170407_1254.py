# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfm_music', '0003_auto_20170404_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='uploadDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='netease',
            name='uploadDate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

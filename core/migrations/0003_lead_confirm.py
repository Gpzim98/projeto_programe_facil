# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160806_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='confirm',
            field=models.CharField(default='', max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-04 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20160926_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulesenrollment',
            name='forum_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

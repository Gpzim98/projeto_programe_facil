# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20161004_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseenrollment',
            name='final_score',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, null=True),
        ),
    ]
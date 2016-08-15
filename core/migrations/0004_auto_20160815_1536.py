# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_lead_confirm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='confirm',
            new_name='code_confirm',
        ),
        migrations.AddField(
            model_name='lead',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]

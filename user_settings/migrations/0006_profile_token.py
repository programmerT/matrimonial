# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import user_settings.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0005_auto_20170428_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='token',
            field=models.CharField(default=user_settings.models.token_generator, editable=False, max_length=20, unique=True),
        ),
    ]

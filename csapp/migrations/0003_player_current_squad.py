# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-23 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csapp', '0002_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='current_squad',
            field=models.BooleanField(default=True),
        ),
    ]

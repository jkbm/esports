# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0030_player_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]

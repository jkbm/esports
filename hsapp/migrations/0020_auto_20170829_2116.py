# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0019_auto_20170829_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='inspire',
        ),
        migrations.RemoveField(
            model_name='card',
            name='taunt',
        ),
        migrations.AddField(
            model_name='card',
            name='cardID',
            field=models.CharField(default='AAA_000', max_length=10),
        ),
    ]

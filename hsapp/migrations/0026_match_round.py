# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 23:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0025_auto_20171005_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='round',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

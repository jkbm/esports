# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0006_auto_20170815_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='win', to='hsapp.Player'),
        ),
    ]

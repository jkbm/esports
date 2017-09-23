# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0007_match_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='players',
            field=models.ManyToManyField(related_name='players', to='hsapp.Player'),
        ),
    ]
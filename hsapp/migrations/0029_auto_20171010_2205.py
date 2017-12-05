# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0028_match_vod_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='presenters',
            field=models.ManyToManyField(related_name='presenters', to='hsapp.Player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, default='media/hsapp/players/user-icon-placeholder_DP8A4SZ.png', null=True, upload_to='hsapp/players'),
        ),
    ]

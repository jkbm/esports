# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0002_player_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(null=True, upload_to='hsapp/static/images/players'),
        ),
    ]
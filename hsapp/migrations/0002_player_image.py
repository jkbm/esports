# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='image',
            field=models.ImageField(null=True, upload_to='players'),
        ),
    ]
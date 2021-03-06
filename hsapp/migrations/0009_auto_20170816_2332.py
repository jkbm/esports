# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 20:32
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0008_tournament_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hsapp/players'),
        ),
    ]

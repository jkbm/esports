# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0011_auto_20170818_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
                ('players', models.ManyToManyField(related_name='group_players', to='hsapp.Player')),
                ('tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hsapp.Tournament')),
            ],
        ),
        migrations.AlterField(
            model_name='match',
            name='score',
            field=models.CharField(default='0-0', max_length=10),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='win', to='hsapp.Player'),
        ),
    ]

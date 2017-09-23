# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hsapp', '0017_tournament_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('text', models.TextField(blank=True, null=True)),
                ('flavortext', models.TextField(blank=True, null=True)),
                ('cost', models.PositiveSmallIntegerField()),
                ('card_set', models.CharField(max_length=30)),
                ('CLASS', models.CharField(choices=[('MAGE', 'Mage'), ('WARRIOR', 'Warrior'), ('WARLOCK', 'Warlock'), ('HUNTER', 'Hunter'), ('PRIEST', 'Priest'), ('DRUID', 'Druid'), ('ROGUE', 'Rogue'), ('PALADIN', 'Paladin'), ('SHAMAN', 'Shaman')], max_length=30)),
                ('cardtype', models.CharField(max_length=30)),
                ('rarity', models.CharField(max_length=30)),
                ('artist', models.CharField(max_length=30)),
                ('collectible', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='hsapp/cards')),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('cards', models.ManyToManyField(to='hsapp.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Deckset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decks', models.ManyToManyField(to='hsapp.Deck')),
                ('tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hsapp.Tournament')),
            ],
        ),
    ]
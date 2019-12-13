# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-11 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0025_storyemit_orgs'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerInfoEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_type', models.PositiveSmallIntegerField(choices=[(0, b'Info'), (1, b'Ruling'), (2, b'Praise'), (3, b'Criticism')], default=0)),
                ('text', models.TextField(blank=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='character.PlayerAccount')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerSiteEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('last_seen', models.DateTimeField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='character.PlayerAccount')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

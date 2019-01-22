# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-13 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0020_auto_20180212_2141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goldpolicy',
            old_name='apc_value',
            new_name='apc_value_max',
        ),
        migrations.AddField(
            model_name='goldpolicy',
            name='apc_note',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='goldpolicy',
            name='apc_value_min',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
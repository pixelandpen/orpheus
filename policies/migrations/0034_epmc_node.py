# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-04 00:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0033_auto_20180904_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='epmc',
            name='node',
            field=models.ForeignKey(default='412582', on_delete=django.db.models.deletion.PROTECT, related_name='epmc_policies', to='policies.Node'),
            preserve_default=False,
        ),
    ]
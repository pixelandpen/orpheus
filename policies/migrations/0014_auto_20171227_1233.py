# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0013_auto_20171227_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greenpolicy',
            name='version_embargo_months',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

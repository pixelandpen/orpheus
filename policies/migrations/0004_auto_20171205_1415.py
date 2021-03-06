# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0003_create_functional_unique_index_for_node_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=10)),
                ('long_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ('short_name',),
            },
        ),
        migrations.AlterModelOptions(
            name='node',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='greenpolicy',
            name='version',
        ),
        migrations.AlterField(
            model_name='node',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='Please select publisher of journal, imprint or conference', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='policies.Node'),
        ),
        migrations.AddField(
            model_name='greenpolicy',
            name='version',
            field=models.ManyToManyField(help_text='Please select all versions this policy applies to', to='policies.Version', verbose_name='versions covered by green policy'),
        ),
    ]

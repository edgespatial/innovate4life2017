# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 21:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0009_supportgroup_year_formed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mother',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.SupportGroup'),
        ),
    ]
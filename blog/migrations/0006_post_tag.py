# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160117_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20160129_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to='%Y/%m/%d'),
        ),
    ]

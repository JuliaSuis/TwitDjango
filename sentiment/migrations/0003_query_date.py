# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0002_auto_20161006_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 23:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0003_query_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='date',
        ),
    ]

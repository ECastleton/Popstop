# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 02:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_location_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]

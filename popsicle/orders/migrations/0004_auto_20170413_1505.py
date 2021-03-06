# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20170412_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='date_added',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AddField(
            model_name='subingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Ingredient'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 04:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20170424_2037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flavor',
            options={'ordering': ['flavor_name']},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['category_name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='flavors',
        ),
        migrations.AddField(
            model_name='flavor',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='orders.ProductCategory'),
        ),
        migrations.AlterField(
            model_name='cateringmenu',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='cateringmenu',
            name='start_date',
            field=models.DateField(),
        ),
    ]

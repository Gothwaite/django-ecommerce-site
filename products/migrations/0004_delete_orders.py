# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 08:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_orders_product_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]

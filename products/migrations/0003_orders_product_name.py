# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160427_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='product_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]

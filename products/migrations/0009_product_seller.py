# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-05 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190804_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

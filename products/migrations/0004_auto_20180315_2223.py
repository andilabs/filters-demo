# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-15 22:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20180315_1752'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductSize',
            new_name='Stock',
        ),
    ]

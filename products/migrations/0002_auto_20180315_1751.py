# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-15 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=4, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='productsize',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Size'),
        ),
    ]

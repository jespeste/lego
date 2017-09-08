# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170829_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='end_date',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='start_date',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
    ]
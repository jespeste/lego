# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 17:32
from __future__ import unicode_literals

import re

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20170908_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(re.compile('^[-a-z0-9æøå_.#%$&/]+\\Z', 32), "Enter a valid 'tag' consisting of letters, numbers, underscores or hyphens.", 'invalid')]),
        ),
    ]
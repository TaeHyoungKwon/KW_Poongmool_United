# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-12 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bamboo', '0003_bamboo_tags1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bamboo',
            old_name='tags1',
            new_name='tags',
        ),
    ]

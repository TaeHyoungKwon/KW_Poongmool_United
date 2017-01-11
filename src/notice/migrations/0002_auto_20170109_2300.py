# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-09 14:00
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='type',
        ),
        migrations.AddField(
            model_name='notice',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

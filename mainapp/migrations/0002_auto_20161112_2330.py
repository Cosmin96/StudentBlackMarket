# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 23:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductDB',
            new_name='Product',
        ),
    ]

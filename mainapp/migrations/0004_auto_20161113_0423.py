# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_uploadfile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UploadFile',
        ),
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(default='mainapp/static/mainapp/production/images/default-avatar.png', upload_to='files/%Y/%m/%d'),
        ),
    ]

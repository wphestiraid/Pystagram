# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-17 08:29
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20171005_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(upload_to='photo_path'),
        ),
    ]
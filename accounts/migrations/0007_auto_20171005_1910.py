# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 10:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20170928_2143'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='relation',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-20 00:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pexam', '0003_auto_20180817_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='wish',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='wish',
            old_name='user_id',
            new_name='wish_id',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-22 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pexam2', '0011_auto_20180822_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='granted',
        ),
        migrations.AlterField(
            model_name='join',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Joining', to='pexam2.Trip'),
        ),
        migrations.AlterField(
            model_name='join',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Joining', to='pexam2.User'),
        ),
    ]

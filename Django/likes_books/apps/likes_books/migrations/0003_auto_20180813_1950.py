# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-13 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0002_remove_book_liked_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='uploader',
            new_name='users_id',
        ),
        migrations.AddField(
            model_name='like',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to='likes_books.Book'),
        ),
        migrations.AddField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Book', to='likes_books.User'),
        ),
    ]

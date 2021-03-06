# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 18:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hobbies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='category',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='category_id',
            new_name='category_map_id',
        ),
        migrations.RenameField(
            model_name='sub_categories',
            old_name='sub_category',
            new_name='sub_category_name',
        ),
        migrations.RenameField(
            model_name='sub_categories_sub_categories1_mapping',
            old_name='sub_category1',
            new_name='sub_category1_id',
        ),
        migrations.RenameField(
            model_name='sub_categories_sub_categories1_mapping',
            old_name='sub_category',
            new_name='sub_category_id',
        ),
    ]

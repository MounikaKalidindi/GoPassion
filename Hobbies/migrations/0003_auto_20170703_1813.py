# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hobbies', '0002_auto_20170703_1810'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisements',
            old_name='category_id',
            new_name='category_map_id',
        ),
        migrations.RenameField(
            model_name='sub_categories1',
            old_name='sub_category1',
            new_name='sub_category1_name',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='category_id',
        ),
        migrations.AddField(
            model_name='feedback',
            name='category_map_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Categories_Sub_Categories_Mapping'),
            preserve_default=False,
        ),
    ]

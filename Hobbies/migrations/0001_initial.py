# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 17:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categories_Sub_Categories_Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=50)),
                ('suggesions', models.CharField(max_length=50)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_adv', models.BooleanField()),
                ('src', models.CharField(max_length=300)),
                ('likes', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Categories_Sub_Categories_Mapping')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('intrest', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Categories')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Categories1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category1', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Categories_Sub_Categories1_Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Sub_Categories')),
                ('sub_category1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Sub_Categories1')),
            ],
        ),
        migrations.CreateModel(
            name='Tutorials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('video', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
                ('sub_category1_map_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Sub_Categories_Sub_Categories1_Mapping')),
            ],
        ),
        migrations.AddField(
            model_name='followers',
            name='follower_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='followers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categories_sub_categories_mapping',
            name='sub_category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Sub_Categories'),
        ),
        migrations.AddField(
            model_name='advertisements',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Categories_Sub_Categories_Mapping'),
        ),
        migrations.AddField(
            model_name='advertisements',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hobbies.Posts'),
        ),
        migrations.AddField(
            model_name='advertisements',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

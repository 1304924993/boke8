# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-12 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0002_articles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=10)),
                ('c_keywords', models.CharField(max_length=10)),
                ('c_describe', models.CharField(max_length=100)),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'column_article',
            },
        ),
    ]
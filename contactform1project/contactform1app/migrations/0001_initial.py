# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-15 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.IntegerField(max_length=100)),
                ('sal', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('loc', models.CharField(max_length=100)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-15 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactform1app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empdata',
            name='ename',
            field=models.CharField(max_length=100),
        ),
    ]

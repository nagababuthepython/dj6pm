# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-02 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otoapp', '0003_auto_20190502_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.OneToOneField(null=True, on_delete=models.SET(3), to='otoapp.student'),
        ),
    ]

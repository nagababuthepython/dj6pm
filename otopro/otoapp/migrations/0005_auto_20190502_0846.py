# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-02 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('otoapp', '0004_auto_20190502_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='otoapp.student'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-12 00:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('app', '0003_auto_20180407_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
        ),
    ]
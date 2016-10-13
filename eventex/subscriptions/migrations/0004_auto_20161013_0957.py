# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import eventex.subscriptions.validators


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_auto_20161009_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='cpf',
            field=models.CharField(max_length=11, validators=[eventex.subscriptions.validators.validate_cpf], verbose_name='cpf'),
        ),
    ]
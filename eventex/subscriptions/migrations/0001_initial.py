# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='cpf')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='telefone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'verbose_name': 'inscrição',
                'verbose_name_plural': 'inscrições',
            },
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-27 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_servicos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicos',
            name='escolha',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
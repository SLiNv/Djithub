# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0003_remove_repository_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='slug',
            field=models.SlugField(),
        ),
    ]

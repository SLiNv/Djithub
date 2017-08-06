# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 03:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repos', '0008_auto_20170625_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='editors',
            field=models.ManyToManyField(blank=True, related_name='editors', to=settings.AUTH_USER_MODEL),
        ),
    ]
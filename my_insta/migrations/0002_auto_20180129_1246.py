# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-29 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_insta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]

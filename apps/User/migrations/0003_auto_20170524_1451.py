# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-24 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecode',
            name='code',
            field=models.IntegerField(default=12345, verbose_name='\u90ae\u7bb1\u9a8c\u8bc1\u7801'),
        ),
    ]

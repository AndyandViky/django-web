# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-24 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Country', '0002_auto_20170523_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrycultural',
            name='detailDress',
            field=models.CharField(default='', max_length=100, verbose_name='\u8be6\u7ec6\u5730\u5740'),
        ),
        migrations.AddField(
            model_name='countryfoods',
            name='detailDress',
            field=models.CharField(default='', max_length=100, verbose_name='\u8be6\u7ec6\u5730\u5740'),
        ),
        migrations.AddField(
            model_name='countryscince',
            name='detailDress',
            field=models.CharField(default='', max_length=100, verbose_name='\u8be6\u7ec6\u5730\u5740'),
        ),
        migrations.AddField(
            model_name='countrytourist',
            name='detailDress',
            field=models.CharField(default='', max_length=100, verbose_name='\u8be6\u7ec6\u5730\u5740'),
        ),
    ]
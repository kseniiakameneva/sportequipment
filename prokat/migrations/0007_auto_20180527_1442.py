# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-27 11:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prokat', '0006_auto_20180525_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_end',
            field=models.DateField(default=datetime.datetime(2018, 5, 27, 11, 42, 53, 688931, tzinfo=utc), verbose_name='Дата начала поездки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ваш комментарий:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 5, 27, 11, 42, 53, 688931, tzinfo=utc), verbose_name='Дата начала поездки'),
        ),
    ]
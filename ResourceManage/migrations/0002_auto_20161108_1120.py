# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceManage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storage',
            name='raidtype',
            field=models.CharField(max_length=30, verbose_name='\u5b58\u50a8RAID\u7c7b\u578b'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='storagename',
            field=models.CharField(unique=True, max_length=100, verbose_name='\u5b58\u50a8\u540d\u79f0', db_index=True),
        ),
        migrations.AlterField(
            model_name='storage',
            name='storagetype',
            field=models.CharField(max_length=30, verbose_name='\u5b58\u50a8\u7c7b\u578b'),
        ),
    ]

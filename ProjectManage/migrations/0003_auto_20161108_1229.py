# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0002_auto_20161108_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='usedcore',
            field=models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5df2\u7528CPU\u6838\u6570', blank=True),
        ),
        migrations.AddField(
            model_name='cluster',
            name='usedmem',
            field=models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5df2\u7528\u5185\u5b58', blank=True),
        ),
        migrations.AddField(
            model_name='cluster',
            name='usedstorage',
            field=models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5df2\u7528\u5b58\u50a8', blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='symem',
            field=models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5269\u4f59\u5185\u5b58', blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='ttmem',
            field=models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5185\u5b58', blank=True),
        ),
    ]

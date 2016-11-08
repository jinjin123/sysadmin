# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='sycore',
            field=models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5269\u4f59CPU\u6838\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='symem',
            field=models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5269\u4f59\u5185\u5b58\u5927\u5c0f', blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='systorage',
            field=models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5269\u4f59\u5b58\u50a8', blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='ttcore',
            field=models.IntegerField(default=0, verbose_name='\u96c6\u7fa4CPU\u6838\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='ttmem',
            field=models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5185\u5b58\u5927\u5c0f', blank=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='ttstorage',
            field=models.IntegerField(default=0, verbose_name='\u96c6\u7fa4\u5b58\u50a8', blank=True),
        ),
    ]

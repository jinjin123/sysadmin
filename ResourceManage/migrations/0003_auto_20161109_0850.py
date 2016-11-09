# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceManage', '0002_auto_20161108_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='storagegroup',
            name='systorage',
            field=models.IntegerField(default=0, verbose_name='\u5b58\u50a8\u7ec4\u5269\u4f59\u5927\u5c0f', blank=True),
        ),
        migrations.AddField(
            model_name='storagegroup',
            name='ttstorage',
            field=models.IntegerField(default=0, verbose_name='\u5b58\u50a8\u7ec4\u5927\u5c0f', blank=True),
        ),
        migrations.AddField(
            model_name='storagegroup',
            name='usedstorage',
            field=models.IntegerField(default=0, verbose_name='\u5b58\u50a8\u7ec4\u5df2\u7528\u5927\u5c0f', blank=True),
        ),
        migrations.AddField(
            model_name='vlangroup',
            name='syip',
            field=models.IntegerField(default=0, verbose_name='\u7f51\u6bb5\u7ec4\u5269\u4f59IP\u4e2a\u6570', blank=True),
        ),
        migrations.AddField(
            model_name='vlangroup',
            name='ttip',
            field=models.IntegerField(default=0, verbose_name='\u7f51\u6bb5\u7ec4IP\u4e2a\u6570', blank=True),
        ),
        migrations.AddField(
            model_name='vlangroup',
            name='usedip',
            field=models.IntegerField(default=0, verbose_name='\u7f51\u6bb5\u7ec4\u5df2\u7528IP\u4e2a\u6570', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceManage', '0002_auto_20161107_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='domainname',
            field=models.CharField(unique=True, max_length=30, verbose_name='\u57df\u540d\u79f0', db_index=True),
        ),
        migrations.AlterField(
            model_name='storage',
            name='storagename',
            field=models.CharField(unique=True, max_length=30, verbose_name='\u5b58\u50a8\u540d\u79f0', db_index=True),
        ),
        migrations.AlterField(
            model_name='storagegroup',
            name='storagegroupname',
            field=models.CharField(unique=True, max_length=30, verbose_name='\u5b58\u50a8\u7ec4\u540d\u79f0', db_index=True),
        ),
        migrations.AlterField(
            model_name='vlan',
            name='vlanname',
            field=models.GenericIPAddressField(unique=True, verbose_name='\u7f51\u6bb5\u540d\u79f0', db_index=True),
        ),
        migrations.AlterField(
            model_name='vlangroup',
            name='vlangroupname',
            field=models.CharField(unique=True, max_length=30, verbose_name='\u7f51\u6bb5\u7ec4\u540d\u79f0', db_index=True),
        ),
    ]

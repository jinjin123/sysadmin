# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0003_auto_20161108_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='storagegroup',
            field=models.OneToOneField(verbose_name='\u96c6\u7fa4\u5b58\u50a8\u7ec4', to='ResourceManage.StorageGroup'),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='vlangroup',
            field=models.OneToOneField(verbose_name='\u96c6\u7fa4\u7f51\u7edc\u7ec4', to='ResourceManage.VlanGroup'),
        ),
    ]

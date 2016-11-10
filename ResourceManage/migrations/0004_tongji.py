# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceManage', '0003_auto_20161109_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='tongji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tongjitype', models.CharField(unique=True, max_length=50, verbose_name='\u7edf\u8ba1\u7c7b\u578b', db_index=True)),
                ('count', models.IntegerField(null=True, verbose_name='\u7edf\u8ba1\u7c7b\u578b', blank=True)),
                ('remark', models.CharField(max_length=200, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'tongji',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm',
            name='cpu',
            field=models.IntegerField(null=True, verbose_name='\u865a\u62df\u673acpu\u6838\u6570', blank=True),
        ),
        migrations.AlterField(
            model_name='vm',
            name='disk',
            field=models.IntegerField(null=True, verbose_name='\u865a\u62df\u673a\u78c1\u76d8\u5927\u5c0f', blank=True),
        ),
        migrations.AlterField(
            model_name='vm',
            name='mem',
            field=models.IntegerField(null=True, verbose_name='\u865a\u62df\u673a\u5185\u5b58\u5927\u5c0f', blank=True),
        ),
    ]

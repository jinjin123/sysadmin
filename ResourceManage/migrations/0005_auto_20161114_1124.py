# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceManage', '0004_tongji'),
    ]

    operations = [
        migrations.AddField(
            model_name='storagegroup',
            name='is_selected',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u7528'),
        ),
        migrations.AddField(
            model_name='vlangroup',
            name='is_selected',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u7528'),
        ),
    ]

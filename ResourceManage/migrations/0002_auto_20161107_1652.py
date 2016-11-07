# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ResourceManage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vlan',
            name='vlanname',
            field=models.GenericIPAddressField(verbose_name='\u7f51\u6bb5\u540d\u79f0'),
        ),
    ]

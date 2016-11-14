# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManage', '0004_auto_20161109_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='storagegroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u96c6\u7fa4\u5b58\u50a8\u7ec4', to='ResourceManage.StorageGroup', null=True),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='vlangroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u96c6\u7fa4\u7f51\u7edc\u7ec4', to='ResourceManage.VlanGroup', null=True),
        ),
        migrations.AlterField(
            model_name='pm',
            name='cluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u6240\u5c5e\u96c6\u7fa4', blank=True, to='ProjectManage.Cluster', null=True),
        ),
        migrations.AlterField(
            model_name='pm',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u6240\u5c5e\u57df', blank=True, to='ResourceManage.Domain', null=True),
        ),
        migrations.AlterField(
            model_name='pm',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u6240\u5c5e\u9879\u76ee', blank=True, to='ProjectManage.Project', null=True),
        ),
        migrations.AlterField(
            model_name='pm',
            name='soft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u5b89\u88c5\u8f6f\u4ef6', blank=True, to='ResourceManage.Software', null=True),
        ),
        migrations.AlterField(
            model_name='pm',
            name='storagegroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u6240\u5c5e\u5b58\u50a8\u7ec4', blank=True, to='ResourceManage.StorageGroup', null=True),
        ),
        migrations.AlterField(
            model_name='pm',
            name='vlangroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7269\u7406\u673a\u6240\u5c5e\u7f51\u7edc\u7ec4', blank=True, to='ResourceManage.VlanGroup', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='createuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u521b\u5efa\u4eba\u5458', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='vm',
            name='cluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u6240\u5c5e\u96c6\u7fa4', blank=True, to='ProjectManage.Cluster', null=True),
        ),
        migrations.AlterField(
            model_name='vm',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u865a\u62df\u673a\u6240\u5c5e\u57df', blank=True, to='ResourceManage.Domain', null=True),
        ),
        migrations.AlterField(
            model_name='vm',
            name='pm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u6240\u5c5e\u7269\u7406\u673a', blank=True, to='ProjectManage.Pm', null=True),
        ),
        migrations.AlterField(
            model_name='vm',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u6240\u5c5e\u9879\u76ee', blank=True, to='ProjectManage.Project', null=True),
        ),
        migrations.AlterField(
            model_name='vm',
            name='soft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u865a\u62df\u673a\u5b89\u88c5\u8f6f\u4ef6', blank=True, to='ResourceManage.Software', null=True),
        ),
    ]

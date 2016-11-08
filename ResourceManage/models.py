#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.db import models

class Vlan(models.Model):
    vlanname=models.GenericIPAddressField(verbose_name=u'网段名称',unique=True, db_index=True)
    startip=models.IntegerField(default=16,verbose_name=u'网段起始IP')
    endip=models.IntegerField(default=254,verbose_name=u'网段结束IP')
    gateway=models.GenericIPAddressField(verbose_name=u'网段网关')
    mask=models.GenericIPAddressField(verbose_name=u'网段掩码')
    remark=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'备注')
    def __unicode__(self):
        return self.vlanname
    class Meta:
        db_table = 'vlan'
        ordering = ['-id']


class VlanGroup(models.Model):
    vlangroupname = models.CharField(max_length=30,verbose_name=u'网段组名称',unique=True, db_index=True)
    vlan = models.ManyToManyField(Vlan,blank=True,verbose_name=u'网段名称')
    remark = models.CharField(max_length=200,blank=True,null=True,verbose_name=u'备注')

    def __unicode__(self):
        return self.vlangroupname
    class Meta:
        db_table = 'vlangroup'
        ordering = ['-id']

class StorageGroup(models.Model):
    storagegroupname = models.CharField(max_length=30,verbose_name=u'存储组名称',unique=True, db_index=True)
    remark=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'备注')

    def __unicode__(self):
        return self.storagegroupname
    class Meta:
        db_table = 'storagegroup'
        ordering = ['-id']

class Storage(models.Model):
    storagename=models.CharField(max_length=100,verbose_name=u'存储名称',unique=True, db_index=True)
    storagesize=models.IntegerField(verbose_name=u'存储大小')
    storagetype=models.CharField(max_length=30,verbose_name=u'存储类型')
    raidtype=models.CharField(max_length=30,verbose_name=u'存储RAID类型')
    storagegroup = models.ForeignKey(StorageGroup,verbose_name=u'存储组名称')
    remark=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'备注')
    def __unicode__(self):
        return self.storagename
    class Meta:
        db_table = 'storage'
        ordering = ['-id']




class Software(models.Model):
    softwarename=models.CharField(max_length=30,verbose_name=u'软件名称')
    version=models.CharField(max_length=30,verbose_name=u'软件版本')
    platform=models.CharField(max_length=30,verbose_name=u'软件平台')
    arch=models.CharField(max_length=10,verbose_name=u'软件架构')
    doc=models.CharField(max_length=100,blank=True,null=True,verbose_name=u'软件安装文档')
    path=models.CharField(max_length=100,blank=True,null=True,verbose_name=u'软件存储路径')
    type=models.CharField(max_length=30,verbose_name=u'类型')
    remark=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'备注')
    def __unicode__(self):
        return self.softwarename
    class Meta:
        db_table = 'software'
        ordering = ['-id']

class Domain(models.Model):
    domainname=models.CharField(max_length=30,verbose_name=u'域名称',unique=True, db_index=True)
    DNS=models.GenericIPAddressField(verbose_name=u'DNS')
    remark=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'备注')
    def __unicode__(self):
        return self.domainname
    class Meta:
        db_table = 'domain'
        ordering = ['-id']

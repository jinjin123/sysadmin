#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.db import models
from UserManage.models import User
from ResourceManage.models import Domain,VlanGroup,StorageGroup,Software

class Project(models.Model):
    env=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'环境')
    projectname=models.CharField(max_length=30,verbose_name=u'项目名称')
    shortname=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'项目简称')
    createuser = models.ForeignKey(User,blank=True,null=True,verbose_name=u'创建人员')
    starttime=models.DateTimeField(blank=True,null=True,verbose_name=u'项目开始时间')
    endtime=models.DateTimeField(blank=True,null=True,verbose_name=u'项目结束时间')
    finishtime=models.DateTimeField(blank=True,null=True,verbose_name=u'项目完成时间')
    reason=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'项目超时理由')
    batch=models.CharField(max_length=10,blank=True,null=True,verbose_name=u'项目批次')
    remark=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'备注')
    def __unicode__(self):
        return self.projectname
    class Meta:
        db_table = 'project'
        ordering = ['-id']


class Cluster(models.Model):
    clustername=models.CharField(max_length=30,unique=True,db_index=True,verbose_name=u'集群名称')
    platform=models.CharField(max_length=30,verbose_name=u'集群平台')
    vcaddress=models.GenericIPAddressField(verbose_name=u'集群VC地址')
    vlangroup=models.ForeignKey(VlanGroup,blank=True,null=True,verbose_name=u'集群网络组')
    storagegroup=models.ForeignKey(StorageGroup,blank=True,null=True,verbose_name=u'集群存储组')
    ttstorage=models.IntegerField(blank=True,null=True,verbose_name=u'集群存储')
    systorage=models.IntegerField(blank=True,null=True,verbose_name=u'集群剩余存储')
    ttcore=models.IntegerField(blank=True,null=True,verbose_name=u'集群CPU核数')
    sycore=models.IntegerField(blank=True,null=True,verbose_name=u'集群剩余CPU核数')
    ttmem=models.IntegerField(blank=True,null=True,verbose_name=u'集群内存大小')
    symem=models.IntegerField(blank=True,null=True,verbose_name=u'集群剩余内存大小')
    remark=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'备注')
    def __unicode__(self):
        return self.clustername
    class Meta:
        db_table = 'cluster'
        ordering = ['-id']
 

class Pm(models.Model):
    pmname=models.CharField(max_length=30,unique=True,db_index=True,verbose_name=u'物理机名称')
    sn=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'物理机序列号')
    cluster=models.ForeignKey(Cluster,blank=True,null=True,verbose_name=u'物理机所属集群')
    project=models.ForeignKey(Project,blank=True,null=True,verbose_name=u'物理机所属项目')
    vlangroup=models.ForeignKey(VlanGroup,blank=True,null=True,verbose_name=u'物理机所属网络组')
    storagegroup=models.ForeignKey(StorageGroup,blank=True,null=True,verbose_name=u'物理机所属存储组')
    role=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'物理机角色')
    type=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'物理机类型')
    cpu=models.IntegerField(blank=True,null=True,verbose_name=u'物理机CPU核数')
    memory=models.IntegerField(blank=True,null=True,verbose_name=u'物理机内存大小')
    disk=models.IntegerField(blank=True,null=True,verbose_name=u'物理机磁盘大小')
    os=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'物理机操作系统')
    soft = models.ForeignKey(Software,blank=True,null=True,verbose_name=u'物理机安装软件')
    eth=models.IntegerField(blank=True,null=True,verbose_name=u'物理机网卡个数')
    hba=models.IntegerField(blank=True,null=True,verbose_name=u'物理机HBA卡个数')
    ip=models.GenericIPAddressField(verbose_name=u'物理机地址')
    ilo_ip=models.GenericIPAddressField(verbose_name=u'物理机管理地址')
    mask= models.GenericIPAddressField(blank=True,null=True,verbose_name=u'物理机子网掩码')
    gateway= models.GenericIPAddressField(blank=True,null=True,verbose_name=u'物理机网关')
    domain=models.ForeignKey(Domain,blank=True,null=True,verbose_name=u'物理机所属域')
    jiguihao=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'物理机机柜号')
    jiguiwei=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'物理机机柜位')
    hba_wwn=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'物理机HBA卡WWN')
    position=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'物理机位置')
    ttstorage=models.IntegerField(blank=True,null=True,verbose_name=u'物理机存储大小')
    systorage=models.IntegerField(blank=True,null=True,verbose_name=u'剩余存储大小')
    sycore=models.IntegerField(blank=True,null=True,verbose_name=u'物理机剩余CPU核数')
    symem=models.IntegerField(blank=True,null=True,verbose_name=u'物理机剩余CPU核数')
    remark=models.CharField(max_length=30,blank=True,null=True,verbose_name=u'备注')
    def __unicode__(self):
        return self.pmname
    class Meta:
        db_table = 'pm'
        ordering = ['-id']


class Vm(models.Model):
    vmname = models.CharField(max_length=30,unique=True,db_index=True,verbose_name=u'虚拟机名称')
    project = models.ForeignKey(Project,blank=True,null=True,verbose_name=u'所属项目')
    pm = models.ForeignKey(Pm,blank=True,null=True,verbose_name=u'所属物理机')
    role = models.CharField(max_length=30,blank=True,null=True,verbose_name=u'虚拟机角色')
    batch = models.CharField(max_length=30,blank=True,null=True,verbose_name=u'虚拟机批次')
    env = models.CharField(max_length=30,blank=True,null=True,verbose_name=u'虚拟机环境')
    cluster = models.ForeignKey(Cluster,blank=True,null=True,verbose_name=u'所属集群')
    os = models.CharField(max_length=30,verbose_name=u'虚拟机操作系统')
    soft = models.ForeignKey(Software,blank=True,null=True,verbose_name=u'虚拟机安装软件')
    cpu = models.IntegerField(blank=True,null=True,verbose_name=u'虚拟机cpu核数')
    mem = models.IntegerField(blank=True,null=True,verbose_name=u'虚拟机内存大小')
    disk = models.IntegerField(blank=True,null=True,verbose_name=u'虚拟机磁盘大小')
    ip = models.GenericIPAddressField(verbose_name=u'虚拟机地址')
    mask = models.GenericIPAddressField(blank=True,null=True,verbose_name=u'虚拟机子网掩码')
    gateway = models.GenericIPAddressField(blank=True,null=True,verbose_name=u'虚拟机网关')
    domain = models.ForeignKey(Domain,blank=True,null=True,verbose_name=u'虚拟机所属域')
    admin = models.CharField(max_length=30,blank=True,null=True,verbose_name=u'虚拟机管理员')
    appuser = models.CharField(max_length=30,blank=True,null=True,verbose_name=u'虚拟机应用用户')
    remark=models.CharField(max_length=200,blank=True,null=True,verbose_name=u'备注')

    def __unicode__(self):
        return self.vmname
    class Meta:
        db_table = 'vm'
        ordering = ['-id']


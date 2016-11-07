#!/usr/bin/env python
#-*- coding: utf-8 -*-
from NetworkManage.models import vlan,vlantype
from ProjectManage.models import vm,cluster

@login_required
@PermissionVerify()
def showip(request,ID):
'''
通过集群ID获取网段类型ID，再通过网段类型ID获取所有关联网段,
通过startip和endip获取每个网段的ip地址，将所有的ip地址存入iplist列表中
'''
    #定义网段类型中所有ip地址列表
    iplist1=[]
    #定义已使用ip地址列表
    iplist2=[]
    #定义网段类型中可用ip地址列表
    iplist3=[]
    vlantype_id= cluster.objects.get(id = ID).vlantype_id
    vlantypeobject = vlantype.objects.get(id=vlantype_id)
    vlanqueryset = vlantypeobject.vlan.all()
    for i in vlanqueryset:
        ip_tmp=i.vlanname.rstrip().split('.')
        ip_suffix=ip_tmp[0]+'.'+ip_tmp[1]+'.'+ip_tmp[2]
	vlan_startip=i.startip
	vlan_endip=i.endip
        for j in range(vlan_startip,vlan_endip+1):
            ip=ip_suffix+'.'+str(j)
            iplist1.append(ip)
    ips=vm.objects.values("ip")
    for i in ips:
        ip1=i['ip']
        iplist2.append(ip1)
    set1 = set(iplist1)    
    set2 = set(iplist2)
    set3 = set1-set2
    iplist3=list(set(set3))
    iplist3.sort()
    return iplist3







    
   

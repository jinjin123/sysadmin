#!/usr/bin/env python
#-*- coding: utf-8 -*-
from ResourceManage.models import Vlan,VlanGroup
from ProjectManage.models import Vm,Cluster,Pm
from django.contrib.auth.decorators import login_required
from UserManage.views.permission import PermissionVerify
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import json

def sort_ip_list(ip_list):
    from IPy import IP
    ip1=[(IP(ip).int(),ip) for ip in ip_list]
    ip1.sort()
    return [ip[1] for ip in ip1]

@login_required
@PermissionVerify()
def getip(request):
        ID= request.GET['ID']
        PID= request.GET['PID']
        ipcount= int(request.GET['ipcount'])

        #定义网段类型中所有ip地址列表
        iplist1=[]
        #定义已使用ip地址列表
        iplist2=[]
        #定义网段类型中可用ip地址列表
        iplist3=[]
        if ID !='':
            vlangroup_id= Cluster.objects.get(id = int(ID)).vlangroup_id
        if PID != '':
            vlangroup_id= Pm.objects.get(id = int(PID)).vlangroup_id
        print vlangroup_id

        vlangroupobject = VlanGroup.objects.get(id=vlangroup_id)
        vlanqueryset = vlangroupobject.vlan.all()
        for i in vlanqueryset:
            ip_tmp=i.vlanname.rstrip().split('.')
            ip_suffix=ip_tmp[0]+'.'+ip_tmp[1]+'.'+ip_tmp[2]
	    vlan_startip=i.startip
	    vlan_endip=i.endip
            for j in range(vlan_startip,vlan_endip+1):
                ip=ip_suffix+'.'+str(j)
                iplist1.append(ip)
        ips=Vm.objects.values("ip")
        for i in ips:
            ip1=i['ip']
            iplist2.append(ip1)
        set1 = set(iplist1)    
        set2 = set(iplist2)
        set3 = set1-set2
        iplist3=list(set(set3))
        iplist=sort_ip_list(iplist3)
        resultdict={}
        ip_tmp=iplist[0].split('.')
        ip_suffix=ip_tmp[0]+'.'+ip_tmp[1]+'.'+ip_tmp[2]
        gateway=Vlan.objects.get(vlanname__contains=ip_suffix).gateway
        mask=Vlan.objects.get(vlanname__contains=ip_suffix).mask
        if ipcount==1:
           resultdict['ip']=iplist[0]
           resultdict['mask']=mask
           resultdict['gateway']=gateway
        elif ipcount==2:
           resultdict['ip']=iplist[0]
           resultdict['vip']=iplist[1]
           resultdict['mask']=mask
           resultdict['gateway']=gateway
        elif ipcount==3:
           resultdict['ip']=iplist[0]
           resultdict['vip']=iplist[1]
           resultdict['scanip']=iplist[2]
           resultdict['mask']=mask
           resultdict['gateway']=gateway
        else:
           pass

        #return HttpResponse(json.dumps(resultdict),content_type='application/json')
        return JsonResponse(resultdict)






    
   

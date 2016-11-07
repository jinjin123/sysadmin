#!/usr/bin/env python
#-*- coding: utf-8 -*-
from ProjectManage.models import Vm,Cluster,Pm

@login_required
@PermissionVerify()
def get(request,ID):
    ttcpu=0
    ttmem=0
    ttstorage=0
    storagegroup_id=Cluster.objects.get(cluster_id = ID).storagegroup_id
    pmqueryset= Pm.objects.get(cluster_id = ID)
    vmqueryset= Vm.objects.get(cluster_id = ID)
    storagequeryset=Storage.objects.get(storagegroup_id = storagegroup_id)

    for i in pmqueryset:
        cpu=i.cpu
        mem=i.mem
        ttcpu=ttcpu+cpu
        ttmem=ttmem+mem

    for j in vmqueryset:
        cpu=j.cpu
        mem=j.mem
        disk=j.mem
        usedcpu=usedcpu+cpu
        usedmem=usedmem+mem
        useddisk=useddisk+disk
        
    for x in storagequeryset:
        storagesize=i.storagesize
        ttstorage=ttstorage+storagesize
    sycore=ttcpu-usedcpu
    symem=ttmem-usedmem
    systorage=ttstorage-useddisk





    





    
   
        







    
   

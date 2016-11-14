#!/usr/bin/env python
#-*- coding: utf-8 -*-
#import paramiko
#import os,hashlib
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from ProjectManage.forms import ClusterForm
from ProjectManage.models import Cluster,Vm,Project,Pm
from ResourceManage.models import Storage,StorageGroup,VlanGroup,Vlan
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@PermissionVerify()
@login_required
def clusterinput(request):
    if request.method == 'POST':
        form = ClusterForm(request.POST)
        if form.is_valid():
            cluster=form.save(commit=False)
            StorageGroup.objects.filter(id=cluster.storagegroup_id).update(is_selected=1)
            VlanGroup.objects.filter(id=cluster.vlangroup_id).update(is_selected=1)
            form.save()
            return HttpResponseRedirect(reverse('clusterlist'))

    else:
        form = ClusterForm()
        form.fields['vlangroup'].queryset=VlanGroup.objects.filter(is_selected=0)
        form.fields['storagegroup'].queryset=StorageGroup.objects.filter(is_selected=0)
    kwvars = {
        'form':form,
        'request':request,
    }
    return render_to_response('ProjectManage/clusterForm.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def clusterlist(request):
    mList = Cluster.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/clusterlist.html',kwvars,RequestContext(request))

@PermissionVerify()
@login_required
def clusterdelete(request,ID):
    cluster=Cluster.objects.filter(id = ID)
    StorageGroup.objects.filter(id=cluster.storagegroup_id).update(is_selected=1)
    VlanGroup.objects.filter(id=cluster.vlangroup_id).update(is_selected=1)
    cluster.delete()

    return HttpResponseRedirect(reverse('clusterlist'))


@PermissionVerify()
@login_required
def clusteredit(request,ID):
    cl= Cluster.objects.get(id = ID)
    StorageGroup.objects.filter(id=cl.storagegroup_id).update(is_selected=0)
    VlanGroup.objects.filter(id=cl.vlangroup_id).update(is_selected=0)

    if request.method=='POST':
        form = ClusterForm(request.POST,instance=cl)
        if form.is_valid():
            cluster=form.save(commit=False)
            StorageGroup.objects.filter(id=cluster.storagegroup_id).update(is_selected=1)
            VlanGroup.objects.filter(id=cluster.vlangroup_id).update(is_selected=1)
            form.save()
            return HttpResponseRedirect(reverse('clusterlist'))
    else:
        form = ClusterForm(instance=cl)
        form.fields['vlangroup'].queryset=VlanGroup.objects.filter(is_selected=0)
        form.fields['storagegroup'].queryset=StorageGroup.objects.filter(is_selected=0)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ProjectManage/clusteredit.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def clustershowpm(request,ID):
    cl= Cluster.objects.get(id = ID)
    
    mList = cl.pm_set.all()


    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/pmlist.html',kwvars,RequestContext(request))

@PermissionVerify()
@login_required
def clustershowvm(request,ID):
    cl= Cluster.objects.get(id = ID)
    
    mList = cl.vm_set.all()


    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/vmlist.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def clusterquery(request):
    if request.GET.has_key("query"):
        kwargs ={}
        clustername = request.GET.get('clustername')
        platform = request.GET.get('platform')
        vcaddress = request.GET.get('vcaddress')
        if clustername != '':
            kwargs['clustername'] = clustername 
        if platform != '':
            kwargs['platform'] = platform 
        if vcaddress != '':
            kwargs['vcaddress'] = vcaddress 
        mList = Cluster.objects.filter(**kwargs)
        print kwargs	

        lst = SelfPaginator(request,mList, 20)

        kwvars = {
            'lPage':lst,
            'request':request,
        }

        return render_to_response('ProjectManage/clusterlist.html',kwvars,RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('clusterflush'))

@login_required
@PermissionVerify()
def clusterflush(request):
    tmpdict={}
    idlist=[]
    ids=Cluster.objects.values("id")
    for i in ids:
        id=i['id']
        idlist.append(id)
    for x in idlist:
        tmpdict[x]=Cluster.objects.get(id = x).storagegroup_id
   
    for ID in tmpdict:
        ttcore=0
        ttmem=0
        ttstorage=0
        sycore=0
        symem=0
        systorage=0
        usedcore=0
        usedmem=0
        usedstorage=0
        storagegroup_id=tmpdict[ID]
 
        pmqueryset= Pm.objects.filter(cluster_id = ID)
        vmqueryset= Vm.objects.filter(cluster_id = ID)
        storagequeryset=Storage.objects.filter(storagegroup_id = storagegroup_id)

        for i in pmqueryset:
            cpu=i.cpu
            mem=i.memory
            ttcore=ttcore+cpu
            ttmem=ttmem+mem

        for j in vmqueryset:
            cpu=j.cpu
            mem=j.mem
            disk=j.disk
            usedcore=usedcore+cpu
            usedmem=usedmem+mem
            usedstorage=usedstorage+disk

        for x in storagequeryset:
            storagesize=x.storagesize
            ttstorage=ttstorage+storagesize

        sycore=ttcore-usedcore
        symem=ttmem-usedmem
        systorage=ttstorage-usedstorage
        Cluster.objects.filter(id=ID).update(ttstorage=ttstorage,systorage=systorage,usedstorage=usedstorage,ttcore=ttcore,sycore=sycore,usedcore=usedcore,ttmem=ttmem,symem=symem,usedmem=usedmem)
        StorageGroup.objects.filter(id=storagegroup_id).update(ttstorage=ttstorage,systorage=systorage,usedstorage=usedstorage)
    mList = Cluster.objects.all()
    lst = SelfPaginator(request,mList, 20)
    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/clusterlist.html',kwvars,RequestContext(request))




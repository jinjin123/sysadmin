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
from ProjectManage.forms import PmForm
from ProjectManage.models import Pm,Cluster,Project
from ResourceManage.models import Storage
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@PermissionVerify()
@login_required
def pminput(request):
    if request.method == 'POST':
        form = PmForm(request.POST)
        if form.is_valid():
            pm = form.save(commit=False)
            if pm.cluster_id != None:
                ttcore=0
                ttmem=0
                usedmem=Cluster.objects.get(id = pm.cluster_id).usedmem
                usedcore=Cluster.objects.get(id = pm.cluster_id).usedcore
                pmqueryset= Pm.objects.filter(cluster_id = pm.cluster_id)
                for i in pmqueryset:
                    cpu=i.cpu
                    mem=i.memory
                    ttcore=ttcore+cpu
                    ttmem=ttmem+mem
                ttcore=ttcore+pm.cpu
                ttmem=ttmem+pm.memory
                sycore=ttcore-usedcore
                symem=ttmem-usedmem
                Cluster.objects.filter(id=pm.cluster_id).update(ttcore=ttcore,ttmem=ttmem,symem=symem,sycore=sycore)

            form.save()
            return HttpResponseRedirect(reverse('pmlist'))

    else:
        form = PmForm()
    kwvars = {
        'form':form,
        'request':request,
    }
    return render_to_response('ProjectManage/pmForm.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def pmlist(request):
    mList = Pm.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/pmlist.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def pmdelete(request,ID):
    bcpm= Pm.objects.get(id = ID)
    bcpmcluster_id=bcpm.cluster_id
    bccpu=bcpm.cpu
    bcmem=bcpm.memory
    bcttcore1=0
    bcttmem1=0
    bcusedcore1=Cluster.objects.get(id =bcpmcluster_id ).usedcore
    bcusedmem1=Cluster.objects.get(id =bcpmcluster_id ).usedmem
    pmqueryset= Pm.objects.filter(cluster_id = bcpmcluster_id)
    for i in pmqueryset:
        cpu=i.cpu
        mem=i.memory
        bcttcore1=bcttcore1+cpu
        bcttmem1=bcttmem1+mem
    bcttcore1=bcttcore1-bccpu
    bcttmem1=bcttmem1-bcmem
    bcsycore1=bcttcore1-bcusedcore1
    bcsymem1=bcttmem1-bcusedmem1
    Cluster.objects.filter(id=bcpmcluster_id).update(ttcore=bcttcore1,sycore=bcsycore1,ttmem=bcttmem1,symem=bcsymem1)
    Pm.objects.filter(id = ID).delete()
 

    return HttpResponseRedirect(reverse('pmlist'))


@PermissionVerify()
@login_required
def pmedit(request,ID):
    bcpm= Pm.objects.get(id = ID)
    bcpmcluster_id=bcpm.cluster_id
    bccpu=bcpm.cpu
    bcmem=bcpm.memory
    if request.method=='POST':
        form = PmForm(request.POST,instance=bcpm)
        if form.is_valid():
            acpm = form.save(commit=False)
            acpmcluster_id=acpm.cluster_id
            print "clusterid"
            print acpmcluster_id
            #物理机变更前后均属于集群
            if bcpmcluster_id != None and acpmcluster_id != None:
                bcttcore1=0
                bcttmem1=0
                bcusedcore1=Cluster.objects.get(id =bcpmcluster_id ).usedcore
                bcusedmem1=Cluster.objects.get(id =bcpmcluster_id ).usedmem
                pmqueryset= Pm.objects.filter(cluster_id = bcpmcluster_id)
                for i in pmqueryset:
                    cpu=i.cpu
                    mem=i.memory
                    bcttcore1=bcttcore1+cpu
                    bcttmem1=bcttmem1+mem
                bcsycore1=bcttcore1-bcusedcore1
                bcsymem1=bcttmem1-bcusedmem1
                accpu=acpm.cpu
                acmem=acpm.memory
                #不变更cluster信息
                if bcpmcluster_id==acpmcluster_id:
                    ttcore=bcttcore1-bccpu+accpu
                    ttmem=bcttmem1-bcmem+acmem
                    sycore=bcsycore1-bccpu+accpu
                    symem=bcsymem1-bcmem+acmem
                    Cluster.objects.filter(id=bcpmcluster_id).update(ttcore=ttcore,sycore=sycore,ttmem=ttmem,symem=symem)
                #变更集群信息 
                else :
                    bcttcore2=Cluster.objects.get(id=acpmcluster_id).ttcore
                    bcsycore2=Cluster.objects.get(id=acpmcluster_id).sycore
                    bcttmem2=Cluster.objects.get(id=acpmcluster_id).ttmem
                    bcsymem2=Cluster.objects.get(id=acpmcluster_id).symem
                    acttcore2=bcttcore2+accpu
                    acsycore2=bcsycore2+accpu
                    acttmem2=bcttmem2+acmem
                    acsymem2=bcsymem2+acmem
                    Cluster.objects.filter(id=acpmcluster_id).update(ttcore=acttcore2,sycore=acsycore2,ttmem=acttmem2,symem=acsymem2)
                    acttcore1=bcttcore1-bccpu
                    acsycore1=bcsycore1-bccpu
                    acttmem1=bcttmem1-bcmem
                    acsymem1=bcsymem1-bcmem
                    Cluster.objects.filter(id=bcpmcluster_id).update(ttcore=acttcore1,sycore=acsycore1,ttmem=acttmem1,symem=acsymem1)
            #从cluster变为单机
            elif bcpmcluster_id != None and acpmcluster_id ==None: 
                bcttcore1=0
                bcttmem1=0
                bcusedcore1=Cluster.objects.get(id =bcpmcluster_id ).usedcore
                bcusedmem1=Cluster.objects.get(id =bcpmcluster_id ).usedmem
                pmqueryset= Pm.objects.filter(cluster_id = bcpmcluster_id)
                for i in pmqueryset:
                    cpu=i.cpu
                    mem=i.memory
                    bcttcore1=bcttcore1+cpu
                    bcttmem1=bcttmem1+mem
                bcttcore1=bcttcore1-bccpu
                bcttmem1=bcttmem1-bcmem

                bcsycore1=bcttcore1-bcusedcore1
                bcsymem1=bcttmem1-bcusedmem1
                Cluster.objects.filter(id=bcpmcluster_id).update(ttcore=bcttcore1,sycore=bcsycore1,ttmem=bcttmem1,symem=bcsymem1)
            #从单机变为集群
            elif bcpmcluster_id == None and acpmcluster_id != None:
                accpu=acpm.cpu
                acmem=acpm.memory
                bcttcore2=Cluster.objects.get(id=acpmcluster_id).ttcore
                bcsycore2=Cluster.objects.get(id=acpmcluster_id).sycore
                bcttmem2=Cluster.objects.get(id=acpmcluster_id).ttmem
                bcsymem2=Cluster.objects.get(id=acpmcluster_id).symem
                acttcore2=bcttcore2+accpu
                acsycore2=bcsycore2+accpu
                acttmem2=bcttmem2+acmem
                acsymem2=bcsymem2+acmem
                Cluster.objects.filter(id=acpmcluster_id).update(ttcore=acttcore2,sycore=acsycore2,ttmem=acttmem2,symem=acsymem2)
            else :
                pass                
            form.save()
            return HttpResponseRedirect(reverse('pmlist'))
    else:
        form = PmForm(instance=bcpm)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ProjectManage/pmedit.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def pmquery(request):
    kwargs ={}
    pmname= request.GET.get('pmname')
    ip = request.GET.get('ip')
    ilo_ip = request.GET.get('ilo_ip')
    cluster = request.GET.get('cluster')
    project = request.GET.get('project')
    if pmname != '':
        kwargs['pmname'] = pmname 
    if ip != '':
        kwargs['ip'] = ip 
    if ilo_ip != '':
        kwargs['ilo_ip'] = ilo_ip 
    if cluster !='':
        try:
            tmpobject=Cluster.objects.get(clustername=cluster)
        except Cluster.DoesNotExist:
            tmpobject={}
        if tmpobject != {}:
            cluster_id=tmpobject.id
            kwargs['cluster_id'] = cluster_id
    if project !='':
        try:
            tmpobject1=Project.objects.get(projectname=project)
        except Project.DoesNotExist:
            tmpobject1={}
        if tmpobject1 !={}:
            project_id=tmpobject1.id
            kwargs['project_id'] = project_id
    mList = Pm.objects.filter(**kwargs)
    print kwargs

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/pmlist.html',kwvars,RequestContext(request))

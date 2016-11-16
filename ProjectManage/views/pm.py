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
from ProjectManage.forms import PmForm,PmQueryForm
from ProjectManage.models import Pm,Cluster,Project
from ResourceManage.models import Storage,StorageGroup,VlanGroup,Vlan
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify
from website.common.export import daochupm

@PermissionVerify()
@login_required
def pminput(request):
    if request.method == 'POST':
        form = PmForm(request.POST)
        if form.is_valid():
            pm = form.save(commit=False)
            if pm.role ==u"物理单机宿主机":
                if pm.storagegroup_id !='':
                    StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                if pm.storagegroup_id !='':
                    VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            elif pm.role ==u"物理单机":
                if pm.storagegroup_id !='':
                    StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                if pm.vlangroup_id !='':
                    VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            else :
                storagegroup_id=Cluster.objects.get(id=pm.cluster_id).storagegroup_id
                vlangroup_id=Cluster.objects.get(id=pm.cluster_id).vlangroup_id
                StorageGroup.objects.filter(id=storagegroup_id).update(is_selected=1)
                VlanGroup.objects.filter(id=vlangroup_id).update(is_selected=1)
                
            form.save()
            return HttpResponseRedirect(reverse('pmlist'))

    else:
        form = PmForm()
        form.fields['vlangroup'].queryset=VlanGroup.objects.filter(is_selected=0)
        form.fields['storagegroup'].queryset=StorageGroup.objects.filter(is_selected=0)
    kwvars = {
        'form':form,
        'request':request,
    }
    return render_to_response('ProjectManage/pmForm.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def pmlist(request):
    form = PmQueryForm()
    mList = Pm.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'form':form,
        'request':request,
    }

    return render_to_response('ProjectManage/pmlist.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def pmdelete(request,ID):
    pm=Pm.objects.get(id=ID)
    if pm.storagegroup_id !='':
        print pm.storagegroup_id
        StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=0)
    if pm.vlangroup_id !='':
        VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=0)
    pm.delete()
 

    return HttpResponseRedirect(reverse('pmlist'))


@PermissionVerify()
@login_required
def pmedit(request,ID):
    bcpm= Pm.objects.get(id = ID)
    if bcpm.storagegroup_id !='':
        StorageGroup.objects.filter(id=bcpm.storagegroup_id).update(is_selected=0)
    if bcpm.vlangroup_id !='':
        VlanGroup.objects.filter(id=bcpm.vlangroup_id).update(is_selected=0)
    
    if request.method=='POST':
        form = PmForm(request.POST,instance=bcpm)
        if form.is_valid():
            pm = form.save(commit=False)
            if pm.role == u"物理单机宿主机":
                StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            elif pm.role == u"物理单机":
                if pm.storagegroup_id !='':
                    StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                if pm.vlangroup_id !='':
                    VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            else :
                storagegroup_id=Cluster.objects.get(id=pm.cluster_id).storagegroup_id
                vlangroup_id=Cluster.objects.get(id=pm.cluster_id).vlangroup_id
                StorageGroup.objects.filter(id=storagegroup_id).update(is_selected=1)
                VlanGroup.objects.filter(id=vlangroup_id).update(is_selected=1)
                            
            form.save()
            return HttpResponseRedirect(reverse('pmlist'))
    else:
        form = PmForm(instance=bcpm)
        form.fields['vlangroup'].queryset=VlanGroup.objects.filter(is_selected=0)
        form.fields['storagegroup'].queryset=StorageGroup.objects.filter(is_selected=0)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ProjectManage/pmedit.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def pmrepl(request,ID):
    bcpm= Pm.objects.get(id = ID)
    if bcpm.storagegroup_id !='':
        StorageGroup.objects.filter(id=bcpm.storagegroup_id).update(is_selected=0)
    if bcpm.vlangroup_id !='':
        VlanGroup.objects.filter(id=bcpm.vlangroup_id).update(is_selected=0)
    if request.method=='POST':
        form = PmForm(request.POST,instance=bcpm)
        if form.is_valid():
            pm = form.save(commit=False)
            if pm.role == u"物理单机宿主机":
                StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            elif pm.role == u"物理单机":
                if pm.storagegroup_id !='':
                    StorageGroup.objects.filter(id=pm.storagegroup_id).update(is_selected=1)
                if pm.vlangroup_id !='':
                    VlanGroup.objects.filter(id=pm.vlangroup_id).update(is_selected=1)
            else :
                storagegroup_id=Cluster.objects.get(id=pm.cluster_id).storagegroup_id
                vlangroup_id=Cluster.objects.get(id=pm.cluster_id).vlangroup_id
                StorageGroup.objects.filter(id=storagegroup_id).update(is_selected=1)
                VlanGroup.objects.filter(id=vlangroup_id).update(is_selected=1)
            form.save()
            return HttpResponseRedirect(reverse('pmlist'))
    else:
        form = PmForm(instance=bcpm)
        form.fields['vlangroup'].queryset=VlanGroup.objects.filter(is_selected=0)
        form.fields['storagegroup'].queryset=StorageGroup.objects.filter(is_selected=0)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ProjectManage/pmrepl.html',kwvars,RequestContext(request))

@PermissionVerify()
@login_required
def pmquery(request):
    kwargs ={}
    pmname= request.GET.get('pmname')
    ip = request.GET.get('ip')
    type = request.GET.get('type')
    role = request.GET.get('role')
    os = request.GET.get('os')
    if pmname != '':
        kwargs['pmname__icontains'] = pmname 
    if ip != '':
        kwargs['ip__contains'] = ip 
    if role != '':
        kwargs['role'] = role 
    if type !='':
            kwargs['type__icontains'] = type
    if os !='':
        kwargs['os__contains'] = os

    mList = Pm.objects.filter(**kwargs)
    form=PmQueryForm()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'form':form,
        'request':request,
    }

    return render_to_response('ProjectManage/pmlist.html',kwvars,RequestContext(request))

@login_required
@PermissionVerify()
def pmexport(request):
    '''物理机信息导出'''
    kwargs ={}
    pmname= request.GET.get('pmname')
    ip = request.GET.get('ip')
    type = request.GET.get('type')
    role = request.GET.get('role')
    os = request.GET.get('os')
    if pmname != '':
        kwargs['pmname__icontains'] = pmname 
    if ip != '':
        kwargs['ip__contains'] = ip 
    if role != '':
        kwargs['role'] = role 
    if type !='':
            kwargs['type__icontains'] = type
    if os !='':
        kwargs['os__contains'] = os
    fnstr=u'pm'
    if kwargs =={}:
        objs=Pm.objects.all()
    else:
        for k in kwargs:
            fnstr=fnstr+'_'+kwargs[k]
        objs = Pm.objects.filter(**kwargs)
    fn=fnstr+'.xls'
    return daochupm(objs,fn)

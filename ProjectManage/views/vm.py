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
from ProjectManage.forms import VmForm
from ProjectManage.models import Vm,Project,Cluster,Pm
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@PermissionVerify()
@login_required
def vminput(request):
    if request.method == 'POST':
        form = VmForm(request.POST)
        if form.is_valid():
            '''
            vm = form.save(commit=False)
            ttstorage=Cluster.objects.get(id = vm.cluster_id).ttstorage
            ttcore=Cluster.objects.get(id = vm.cluster_id).ttcore
            ttmem=Cluster.objects.get(id = vm.cluster_id).ttmem
            usedstorage=Cluster.objects.get(id = vm.cluster_id).usedstorage
            usedcore=Cluster.objects.get(id = vm.cluster_id).usedcore
            usedmem=Cluster.objects.get(id = vm.cluster_id).usedcore
            usedstorage=usedstorage+vm.disk
            usedcore=usedcore+vm.cpu
            usedmem=usedmem+vm.mem
            systorage=ttstorage-usedstorage
            sycore=ttcore-usedcore
            symem=ttmem-usedmem
            Cluster.objects.filter(id=vm.cluster_id).update(usedcore=usedcore,usedstorage=usedstorage,usedmem=usedmem,sycore=sycore,symem=symem,systorage=systorage)
            '''
            vm = form.save(commit=False)
            vm.batch=Project.objects.get(id=vm.project_id).batch
            vm.env=Project.objects.get(id=vm.project_id).env
            form.save()
            return HttpResponseRedirect(reverse('vmlist'))

    else:
        form = VmForm()
        form.fields['pm'].queryset=Pm.objects.filter(role="物理单机宿主机")
    kwvars = {
        'form':form,  
        'request':request,
    }
    return render_to_response('ProjectManage/vmForm.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def vmlist(request):
    mList = Vm.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/vmlist.html',kwvars,RequestContext(request))

@PermissionVerify()
@login_required
def vmdelete(request,ID):
    Vm.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('vmlist'))


@PermissionVerify()
@login_required
def vmedit(request,ID):
    pj= Vm.objects.get(id = ID)

    if request.method=='POST':
        form = VmForm(request.POST,instance=pj)
        if form.is_valid():
            vm = form.save(commit=False)
            vm.batch=Project.objects.get(id=vm.project_id).batch
            vm.env=Project.objects.get(id=vm.project_id).env
            form.save()
            return HttpResponseRedirect(reverse('vmlist'))
    else:
        form = VmForm(instance=pj)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ProjectManage/vmedit.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def vmrepl(request,ID):
    pj= Vm.objects.get(id = ID)

    if request.method=='POST':
        form = VmForm(request.POST,instance=pj)
        if form.is_valid():
            vm = form.save(commit=False)
            vm.batch=Project.objects.get(id=vm.project_id).batch
            vm.env=Project.objects.get(id=vm.project_id).env
            form.save()
            return HttpResponseRedirect(reverse('vmlist'))
    else:
        form = VmForm(instance=pj)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ProjectManage/vmForm.html',kwvars,RequestContext(request))



@PermissionVerify()
@login_required
def vmquery(request):
    kwargs ={}
    vmname = request.GET.get('vmname')
    project = request.GET.get('project')
    ip = request.GET.get('ip')
    role = request.GET.get('role')
    os = request.GET.get('os')
    if vmname != '':
        kwargs['vmname__contains'] = vmname 
    if ip != '':
        kwargs['ip__contains'] = ip 
    if role != '':
        kwargs['role__contains'] = role
    if os != '':
        kwargs['os__contains'] = os 
    if project !='':
        try:
            tmpobject=Project.objects.get(projectname=project)
        except Project.DoesNotExist:
            tmpobject1={}
        if tmpobject !={}:
            project_id=tmpobject.id
            kwargs['project_id'] = project_id
    mList = Vm.objects.filter(**kwargs)
    print kwargs

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/vmlist.html',kwvars,RequestContext(request))

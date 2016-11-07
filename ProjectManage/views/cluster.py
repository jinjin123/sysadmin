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
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@PermissionVerify()
@login_required
def clusterinput(request):
    if request.method == 'POST':
        form = ClusterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('clusterlist'))

    else:
        form = ClusterForm()
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
    Cluster.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('clusterlist'))


@PermissionVerify()
@login_required
def clusteredit(request,ID):
    cl= Cluster.objects.get(id = ID)

    if request.method=='POST':
        form = ClusterForm(request.POST,instance=cl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('clusterlist'))
    else:
        form = ClusterForm(instance=cl)

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
    
    mList = cl.Pm_set.all()


    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/pmlist.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def clusterquery(request):
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

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/clusterlist.html',kwvars,RequestContext(request))

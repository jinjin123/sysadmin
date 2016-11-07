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
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@PermissionVerify()
@login_required
def pminput(request):
    if request.method == 'POST':
        form = PmForm(request.POST)
        if form.is_valid():
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
    Pm.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('pmlist'))


@PermissionVerify()
@login_required
def pmedit(request,ID):
    pj= Pm.objects.get(id = ID)

    if request.method=='POST':
        form = PmForm(request.POST,instance=pj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pmlist'))
    else:
        form = PmForm(instance=pj)

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

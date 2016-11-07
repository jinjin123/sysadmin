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
from ResourceManage.forms import SoftwareForm
from ResourceManage.models import Software
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@PermissionVerify()
@login_required
def softwareinput(request):
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('softwarelist'))

    else:
        form = SoftwareForm()
    kwvars = {
        'form':form,
        'request':request,
    }
    return render_to_response('ResourceManage/softwareForm.html',kwvars,RequestContext(request))



@PermissionVerify()
@login_required
def softwarelist(request):
    mList = Software.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ResourceManage/softwarelist.html',kwvars,RequestContext(request))

@PermissionVerify()
@login_required
def softwaredelete(request,ID):
    Software.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('softwarelist'))

@PermissionVerify()
@login_required
def softwareedit(request,ID):
    soft= Software.objects.get(id = ID)

    if request.method=='POST':
        form = SoftwareForm(request.POST,instance=soft)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('softwarelist'))
    else:
        form = SoftwareForm(instance=soft)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ResourceManage/softwareedit.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def softwarequery(request):
    kwargs ={}
    softwarename = request.GET.get('softwarename')
    version = request.GET.get('version')
    platform = request.GET.get('platform')
    arch = request.GET.get('arch')
    type = request.GET.get('type')
    if softwarename != '':
        kwargs['softwarename'] = softwarename 
    if version != '':
        kwargs['version'] = version
    if platform != '':
        kwargs['platform'] = platform 
    if arch != '':
        kwargs['arch'] = arch
    if type != '':
        kwargs['type'] = type 
    mList = Software.objects.filter(**kwargs)
    print kwargs

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ResourceManage/softwarelist.html',kwvars,RequestContext(request))

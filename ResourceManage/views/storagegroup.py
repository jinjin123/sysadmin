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
from ResourceManage.forms import StorageGroupForm
from ResourceManage.models import StorageGroup
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@PermissionVerify()
@login_required
def storagegroupinput(request):
    if request.method == 'POST':
        form = StorageGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('storagegrouplist'))

    else:
        form = StorageGroupForm()
    kwvars = {
        'form':form,
        'request':request,
    }
    return render_to_response('ResourceManage/storagegroupForm.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def storagegrouplist(request):
    mList = StorageGroup.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ResourceManage/storagegrouplist.html',kwvars,RequestContext(request))

@PermissionVerify()
@login_required
def storagegroupdelete(request,ID):
    StorageGroup.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('storagegrouplist'))


@PermissionVerify()
@login_required
def storagegroupedit(request,ID):
    cl= StorageGroup.objects.get(id = ID)

    if request.method=='POST':
        form = StorageGroupForm(request.POST,instance=cl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('storagegrouplist'))
    else:
        form = StorageGroupForm(instance=cl)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ResourceManage/storagegroupedit.html',kwvars,RequestContext(request))





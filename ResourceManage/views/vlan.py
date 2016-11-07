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
from ResourceManage.forms import VlanForm
from ResourceManage.models import Vlan
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@PermissionVerify()
@login_required
def vlaninput(request):
    if request.method == 'POST':
        form = VlanForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vlanlist'))

    else:
        form = VlanForm()
    kwvars = {
        'form':form,
        'request':request,
    }
    return render_to_response('ResourceManage/vlanForm.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def vlanlist(request):
    mList = Vlan.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ResourceManage/vlanlist.html',kwvars,RequestContext(request))

@PermissionVerify()
@login_required
def vlandelete(request,ID):
    Vlan.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('vlanlist'))


@PermissionVerify()
@login_required
def vlanedit(request,ID):
    cl= Vlan.objects.get(id = ID)

    if request.method=='POST':
        form = VlanForm(request.POST,instance=cl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vlanlist'))
    else:
        form = VlanForm(instance=cl)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ResourceManage/vlanedit.html',kwvars,RequestContext(request))





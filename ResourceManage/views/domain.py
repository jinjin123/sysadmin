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
from ResourceManage.forms import DomainForm
from ResourceManage.models import Domain
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@PermissionVerify()
@login_required
def domaininput(request):
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('domainlist'))

    else:
        form = DomainForm()
    kwvars = {
        'form':form,
        'request':request,
    }
    return render_to_response('ResourceManage/domainForm.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def domainlist(request):
    mList = Domain.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ResourceManage/domainlist.html',kwvars,RequestContext(request))

@PermissionVerify()
@login_required
def domaindelete(request,ID):
    Domain.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('domainlist'))


@PermissionVerify()
@login_required
def domainedit(request,ID):
    cl= Domain.objects.get(id = ID)

    if request.method=='POST':
        form = DomainForm(request.POST,instance=cl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('domainlist'))
    else:
        form = DomainForm(instance=cl)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ResourceManage/domainedit.html',kwvars,RequestContext(request))





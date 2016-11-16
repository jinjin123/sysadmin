#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from ResourceManage.forms import StorageForm
from ResourceManage.models import Storage
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify


@PermissionVerify()
@login_required
def storageinput(request):
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('storagelist'))
    else:
        form = StorageForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/storageForm.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def storagelist(request):
    mlist = Storage.objects.all()
    # 分页功能
    lst = SelfPaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ResourceManage/storagelist.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def storagedelete(request, ID):
    Storage.objects.filter(id=ID).delete()
    return HttpResponseRedirect(reverse('storagelist'))


@PermissionVerify()
@login_required
def storageedit(request, ID):
    bcstorage = Storage.objects.get(id=ID)
    if request.method == 'POST':
        form = StorageForm(request.POST,instance=bcstorage)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('storagelist'))
    else:
        form = StorageForm(instance=bcstorage)
    kwvars = {
        'ID': ID,
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/storageedit.html', kwvars, RequestContext(request))





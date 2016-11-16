#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from ResourceManage.forms import VlanGroupForm
from ResourceManage.models import VlanGroup
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify


@PermissionVerify()
@login_required
def vlangroupinput(request):
    if request.method == 'POST':
        form = VlanGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vlangrouplist'))
    else:
        form = VlanGroupForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/vlangroupForm.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def vlangrouplist(request):
    mlist = VlanGroup.objects.all()
    # 分页功能
    lst = SelfPaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ResourceManage/vlangrouplist.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def vlangroupdelete(request, ID):
    VlanGroup.objects.filter(id=ID).delete()
    return HttpResponseRedirect(reverse('vlangrouplist'))


@PermissionVerify()
@login_required
def vlangroupedit(request, ID):
    cl = VlanGroup.objects.get(id=ID)
    if request.method == 'POST':
        form = VlanGroupForm(request.POST, instance=cl)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vlangrouplist'))
    else:
        form = VlanGroupForm(instance=cl)
    kwvars = {
        'ID': ID,
        'form': form,
        'request': request,
    }
    return render_to_response('ResourceManage/vlangroupedit.html', kwvars, RequestContext(request))





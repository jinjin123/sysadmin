#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.contrib.auth.decorators import login_required
from ProjectManage.forms import VmForm
from ProjectManage.models import Vm
from ProjectManage.models import Project
from ProjectManage.models import Pm
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify
from website.common.export import daochuvm
from ProjectManage.views.getinfo import get_info
from ProjectManage.views.getinfo import get_ping
import json


@PermissionVerify()
@login_required
def vminput(request):
    """虚拟机录入"""
    if request.method == 'POST':
        form = VmForm(request.POST)
        if form.is_valid():
            vm = form.save(commit=False)
            vm.batch = Project.objects.get(id=vm.project_id).batch
            vm.env = Project.objects.get(id=vm.project_id).env
            form.save()
            return HttpResponseRedirect(reverse('vmlist'))
    else:
        form = VmForm()
        form.fields['pm'].queryset = Pm.objects.filter(role="物理单机宿主机")
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/vmForm.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def vmlist(request):
    """虚拟机展示"""
    mlist = Vm.objects.all()
    # 分页功能
    lst = SelfPaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/vmlist.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def vmdelete(request, ID):
    """虚拟机删除"""
    Vm.objects.filter(id=ID).delete()
    return HttpResponseRedirect(reverse('vmlist'))


@PermissionVerify()
@login_required
def vmedit(request,ID):
    """虚拟机编辑"""
    pj = Vm.objects.get(id=ID)
    if request.method == 'POST':
        form = VmForm(request.POST, instance=pj)
        if form.is_valid():
            vm = form.save(commit=False)
            vm.batch = Project.objects.get(id=vm.project_id).batch
            vm.env = Project.objects.get(id=vm.project_id).env
            form.save()
            return HttpResponseRedirect(reverse('vmlist'))
    else:
        form = VmForm(instance=pj)
    kwvars = {
        'ID': ID,
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/vmedit.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def vmrepl(request,ID):
    """虚拟机复制"""
    pj = Vm.objects.get(id=ID)
    if request.method == 'POST':
        form = VmForm(request.POST, instance=pj)
        if form.is_valid():
            vm = form.save(commit=False)
            vm.batch = Project.objects.get(id=vm.project_id).batch
            vm.env = Project.objects.get(id=vm.project_id).env
            form.save()
            return HttpResponseRedirect(reverse('vmlist'))
    else:
        form = VmForm(instance=pj)
    kwvars = {
        'ID': ID,
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/vmForm.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def vmquery(request):
    """虚拟机查询"""
    kwargs = {}
    vmname = request.GET.get('vmname')
    project = request.GET.get('project')
    ip = request.GET.get('ip')
    role = request.GET.get('role')
    os = request.GET.get('os')
    if vmname != '':
        kwargs['vmname__icontains'] = vmname 
    if ip != '':
        kwargs['ip__contains'] = ip 
    if role != '':
        kwargs['role__icontains'] = role
    if os != '':
        kwargs['os__icontains'] = os 
    if project != '':
            kwargs['project__projectname__icontains'] = project
    print kwargs
    mlist = Vm.objects.filter(**kwargs)
    # 分页功能
    lst = SelfPaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/vmlist.html', kwvars, RequestContext(request))


@login_required
@PermissionVerify()
def vmexport(request):
    """虚拟机信息导出"""
    kwargs = {}
    vmname = request.GET.get('vmname')
    project = request.GET.get('project')
    ip = request.GET.get('ip')
    role = request.GET.get('role')
    os = request.GET.get('os')
    if vmname != '':
        kwargs['vmname__icontains'] = vmname 
    if ip != '':
        kwargs['ip__contains'] = ip 
    if role != '':
        kwargs['role__icontains'] = role
    if os != '':
        kwargs['os__icontains'] = os 
    if project != '':
            kwargs['project__projectname__icontains'] = project
    fnstr = u'vm'
    if kwargs == {}:
        objs = Vm.objects.all()
    else:
        for k in kwargs:
            fnstr = fnstr+'_'+kwargs[k]
        objs = Vm.objects.filter(**kwargs)
    fn = fnstr+'.xls'
    return daochuvm(objs, fn)



@login_required
@PermissionVerify()
def vmupdate(request,ID):
    """虚拟机信息更新"""
    server = Vm.objects.get(id=ID)
    data = get_info(server.ip)
    data1 = get_ping(server.ip)
    server.vmname = data['hostname']
    server.cpu = data['cpu_count']
    server.mem = data['mem']
    server.os = data['os']
    server.uptime = data['uptime']
    server.disk = data['disktotal']
    server.diskmount = data['diskmount']
    server.kernel = data['os_kernel']
    server.pycpu = data['cpu_core']
    server.arch = data['ansible_machine']
    if data1['ping'] == u'pong':
        server.vmstatus = True

    server.save()
    return HttpResponseRedirect(reverse('vmlist'))







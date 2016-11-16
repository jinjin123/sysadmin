#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from django.shortcuts import render
from django.core.urlresolvers import reverse
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from ProjectManage.forms import ProjectForm, ProjectQueryForm
from ProjectManage.models import Project
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify


@PermissionVerify()
@login_required
def projectinput(request):
    """项目录入"""
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projectlist'))
    else:
        form = ProjectForm()
    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/projectForm.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def projectlist(request):
    """项目展示"""
    form = ProjectQueryForm()
    mlist = Project.objects.all()
    # 分页功能
    lst = SelfPaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/projectlist.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def projectdelete(request, ID):
    """项目删除"""
    Project.objects.filter(id=ID).delete()
    return HttpResponseRedirect(reverse('projectlist'))


@PermissionVerify()
@login_required
def projectedit(request, ID):
    """项目编辑"""
    pj = Project.objects.get(id=ID)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=pj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projectlist'))
    else:
        form = ProjectForm(instance=pj)
    kwvars = {
        'ID': ID,
        'form': form,
        'request': request,
    }
    return render_to_response('ProjectManage/projectedit.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def projectshowvm(request, ID):
    """通过项目ID查询所属虚拟机"""
    pj = Project.objects.get(id=ID)
    mlist = pj.vm_set.all()
    # 分页功能
    lst = SelfPaginator(request, mlist, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }
    return render_to_response('ProjectManage/vmlist.html', kwvars, RequestContext(request))


@PermissionVerify()
@login_required
def projectquery(request):
    """项目查询"""
    kwargs = {}
    env = request.GET.get('env')
    shortname = request.GET.get('shortname')
    projectname = request.GET.get('projectname')
    batch = request.GET.get('batch')
    createuser = request.GET.get('createuser')
    if env != '':
        kwargs['env__contains'] = env 
    if shortname != '':
        kwargs['shortname__contains'] = shortname 
    if projectname != '':
        kwargs['projectname__contains'] = projectname 
    if batch != '':
        kwargs['batch__contains'] = batch
    if createuser != '':
            kwargs['createuser_id'] = createuser
    mlist = Project.objects.filter(**kwargs)
    # 分页功能
    lst = SelfPaginator(request, mlist, 20)
    form = ProjectQueryForm()
    kwvars = {
        'lPage': lst,
        'request': request,
        'form': form,
    }
    return render_to_response('ProjectManage/projectlist.html', kwvars, RequestContext(request))

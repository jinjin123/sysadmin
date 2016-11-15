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
from ProjectManage.forms import ProjectForm
from ProjectManage.models import Project,Vm
from UserManage.models import User
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify


@PermissionVerify()
@login_required
def projectinput(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projectlist'))

    else:
        form = ProjectForm()
    kwvars = {
        'form':form,
        'request':request,
    }
    return render_to_response('ProjectManage/projectForm.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def projectlist(request):
    mList = Project.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/projectlist.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def projectdelete(request,ID):
    Project.objects.filter(id = ID).delete()

    return HttpResponseRedirect(reverse('projectlist'))


@PermissionVerify()
@login_required
def projectedit(request,ID):
    pj= Project.objects.get(id = ID)

    if request.method=='POST':
        form = ProjectForm(request.POST,instance=pj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('projectlist'))
    else:
        form = ProjectForm(instance=pj)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ProjectManage/projectedit.html',kwvars,RequestContext(request))

@PermissionVerify()
@login_required
def projectshowvm(request,ID):
    pj= Project.objects.get(id = ID)
    
    mList = pj.vm_set.all()


    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/vmlist.html',kwvars,RequestContext(request))

@PermissionVerify()
@login_required
def projectquery(request):
    kwargs ={}
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
    if createuser !='':
        try:
            tmpobject=User.objects.get(username=createuser)
        except User.DoesNotExist:
            tmpobject={}
        if tmpobject !={}:
            createuser_id=tmpobject.id
            kwargs['createuser_id'] = createuser_id 
    

    mList = Project.objects.filter(**kwargs)
    print kwargs	

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ProjectManage/projectlist.html',kwvars,RequestContext(request))

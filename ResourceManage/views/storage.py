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
from ResourceManage.forms import StorageForm
from ResourceManage.models import Storage
from ProjectManage.models import Cluster
from website.common.CommonPaginator import SelfPaginator
from UserManage.views.permission import PermissionVerify

@PermissionVerify()
@login_required
def storageinput(request):
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            storage = form.save(commit=False)
            ttstorage=0
            
            usedstorage=Cluster.objects.get(storagegroup_id = storage.storagegroup_id).usedstorage
            storagequeryset=Storage.objects.filter(storagegroup_id =storage.storagegroup_id)
            for x in storagequeryset:
                storagesize=x.storagesize
                ttstorage=ttstorage+storagesize
            ttstorage=ttstorage+storage.storagesize
            systorage=ttstorage-usedstorage
            Cluster.objects.filter(storagegroup_id=storage.storagegroup_id).update(ttstorage=ttstorage,systorage=systorage) 
            form.save()
            return HttpResponseRedirect(reverse('storagelist'))

    else:
        form = StorageForm()
    kwvars = {
        'form':form,
        'request':request,
    }
    return render_to_response('ResourceManage/storageForm.html',kwvars,RequestContext(request))


@PermissionVerify()
@login_required
def storagelist(request):
    mList = Storage.objects.all()

    #分页功能
    lst = SelfPaginator(request,mList, 20)

    kwvars = {
        'lPage':lst,
        'request':request,
    }

    return render_to_response('ResourceManage/storagelist.html',kwvars,RequestContext(request))

@PermissionVerify()
@login_required
def storagedelete(request,ID):
    storagegroup_id=Storage.objects.get(id=ID).storagegroup_id
    ttstorage=Cluster.objects.get(storagegroup_id=storagegroup_id).ttstorage
    systorage=Cluster.objects.get(storagegroup_id=storagegroup_id).systorage
    storagesize=Storage.objects.get(id=ID).storagesize
    ttstorage=ttstorage-storagesize 
    systorage=systorage-storagesize 
    Cluster.objects.filter(storagegroup_id=storagegroup_id).update(ttstorage=ttstorage,systorage=systorage)
    Storage.objects.filter(id = ID).delete()
 
    return HttpResponseRedirect(reverse('storagelist'))


@PermissionVerify()
@login_required
def storageedit(request,ID):
    bcstorage= Storage.objects.get(id = ID)
    bcstoragesize=bcstorage.storagesize
    bcstoragegroup_id=bcstorage.storagegroup_id

    bcttstorage1=0
    bcusedstorage1=Cluster.objects.get(storagegroup_id = bcstoragegroup_id).usedstorage
    storagequeryset=Storage.objects.filter(storagegroup_id =bcstoragegroup_id)
    for x in storagequeryset:
        storagesize=x.storagesize
        bcttstorage1=bcttstorage1+storagesize

    bcsystorage1=bcttstorage1-bcusedstorage1

    if request.method=='POST':
        form = StorageForm(request.POST,instance=bcstorage)
        if form.is_valid():
            acstorage = form.save(commit=False)
            acstoragesize=acstorage.storagesize
            acstoragegroup_id=acstorage.storagegroup_id
            if acstoragegroup_id == bcstoragegroup_id :
                ttstorage=bcttstorage1-bcstoragesize+acstoragesize
                systorage=bcsystorage1-bcstoragesize+acstoragesize
                Cluster.objects.filter(storagegroup_id=bcstoragegroup_id).update(ttstorage=ttstorage,systorage=systorage)
            else :
                bcttstorage2=Cluster.objects.get(storagegroup_id=acstoragegroup_id).ttstorage
                bcsystorage2=Cluster.objects.get(storagegroup_id=acstoragegroup_id).systorage
                acttstorage2=bcttstorage2+acstoragesize
                acsystorage2=bcsystorage2+acstoragesize
                Cluster.objects.filter(storagegroup_id=acstoragegroup_id).update(ttstorage=acttstorage2,systorage=acsystorage2)
                acttstorage1=bcttstorage1-bcstoragesize
                acsystorage1=bcsystorage1-bcstoragesize
                Cluster.objects.filter(storagegroup_id=bcstoragegroup_id).update(ttstorage=acttstorage1,systorage=acsystorage1)

                 
            form.save()
            return HttpResponseRedirect(reverse('storagelist'))
    else:
        form = StorageForm(instance=bcstorage)

    kwvars = {
        'ID':ID,
        'form':form,
        'request':request,
    }

    return render_to_response('ResourceManage/storageedit.html',kwvars,RequestContext(request))





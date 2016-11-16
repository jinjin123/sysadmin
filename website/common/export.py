#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlsxwriter
import xlwt
from django.http import HttpResponse
import time,StringIO,datetime

def daochu(objs,fn):
    output = StringIO.StringIO()
    book = xlsxwriter.Workbook(output)
    sheet = book.add_worksheet()
    data = list(objs.values())
    styles = {'datetime': book.add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'}),
              'date': book.add_format({'num_format': 'yyyy-mm-dd'}),
              'time': book.add_format({'num_format': 'hh:mm:ss'}),
              'header': book.add_format({'bg_color':'#73b5d9','font': 'name Times New Roman', 'color': 'black', 'bold': 'on', 'num_format': '#,##0.00'}),
              'default': book.add_format()
             }
    cell_style = styles['default']
    for cx, v in enumerate(data[0]):
        sheet.write(0, cx, v, styles['header'])
    for rowx, row in enumerate(data):
        for colx, value in enumerate(row):
            if isinstance(row[value], datetime.datetime):
                cell_style = styles['datetime']
            elif isinstance(row[value], datetime.date):
                cell_style = styles['date']
            elif isinstance(row[value], datetime.time):
                cell_style = styles['time']
            else:
                cell_style = styles['default']
            sheet.write(rowx + 1, colx, row[value], cell_style)
    book.close()
    output.seek(0)
    response = HttpResponse(output.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=%s' %fn
    return response

def daochucluster(objs,fn):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet(u'集群信息')
    sheet.write(0,0,'编号')
    sheet.write(0,1,'集群名')
    sheet.write(0,2,'平台')
    sheet.write(0,3,'管理地址')
    sheet.write(0,4,'总存储')
    sheet.write(0,5,'可用存储')
    sheet.write(0,6,'已用存储')
    sheet.write(0,7,'总核数')
    sheet.write(0,8,'可用核数')
    sheet.write(0,9,'已用核数')
    sheet.write(0,10,'总内存')
    sheet.write(0,11,'可用内存')
    sheet.write(0,12,'已用内存')
    sheet.write(0,13,'所属存储组')
    sheet.write(0,14,'所属网络组')
    sheet.write(0,15,'备注')

    row =1
    for i in objs:
        sheet.write(row,0,i.id)
        sheet.write(row,1,i.clustername)
        sheet.write(row,2,i.platform)
        sheet.write(row,3,i.vcaddress)
        sheet.write(row,4,i.ttstorage)
        sheet.write(row,5,i.systorage)
        sheet.write(row,6,i.usedstorage)
        sheet.write(row,7,i.ttcore)
        sheet.write(row,8,i.sycore)
        sheet.write(row,9,i.usedcore)
        sheet.write(row,10,i.ttmem)
        sheet.write(row,11,i.symem)
        sheet.write(row,12,i.usedmem)
        sheet.write(row,13,i.storagegroup_id)
        sheet.write(row,14,i.vlangroup_id)
        sheet.write(row,15,i.remark)
        row=row+1
    output = StringIO.StringIO()
    book.save(output)
    output.seek(0)
    response = HttpResponse(output.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=%s' %fn
    return response

def daochuvm(objs,fn):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet(u'虚拟机信息')
    sheet.write(0,0,'编号')
    sheet.write(0,1,'虚拟机名称')
    sheet.write(0,2,'所属物理机')
    sheet.write(0,3,'所属集群')
    sheet.write(0,4,'所属项目')
    sheet.write(0,5,'角色')
    sheet.write(0,6,'批次')
    sheet.write(0,7,'环境')
    sheet.write(0,8,'操作系统')
    sheet.write(0,9,'安装软件')
    sheet.write(0,10,'CPU')
    sheet.write(0,11,'内存')
    sheet.write(0,12,'磁盘')
    sheet.write(0,13,'IP地址')
    sheet.write(0,14,'子网掩码')
    sheet.write(0,15,'网关')
    sheet.write(0,16,'所属域')
    sheet.write(0,17,'管理员')
    sheet.write(0,18,'应用用户')
    sheet.write(0,19,'备注')

    row =1
    for i in objs:
        sheet.write(row,0,i.id)
        sheet.write(row,1,i.vmname)
        sheet.write(row,2,i.pm_id)
        sheet.write(row,3,i.cluster_id)
        sheet.write(row,4,i.project_id)
        sheet.write(row,5,i.role)
        sheet.write(row,6,i.batch)
        sheet.write(row,7,i.env)
        sheet.write(row,8,i.os)
        sheet.write(row,9,i.soft_id)
        sheet.write(row,10,i.cpu)
        sheet.write(row,11,i.mem)
        sheet.write(row,12,i.disk)
        sheet.write(row,13,i.ip)
        sheet.write(row,14,i.mask)
        sheet.write(row,15,i.gateway)
        sheet.write(row,16,i.domain_id)
        sheet.write(row,17,i.admin)
        sheet.write(row,18,i.appuser)
        sheet.write(row,19,i.remark)
        row=row+1
    output = StringIO.StringIO()
    book.save(output)
    output.seek(0)
    response = HttpResponse(output.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=%s' %fn
    return response

def daochupm(objs,fn):
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet(u'物理机信息')
    sheet.write(0,0,'编号')
    sheet.write(0,1,'物理机名称')
    sheet.write(0,2,'序列号')
    sheet.write(0,3,'功能')
    sheet.write(0,4,'设备类型')
    sheet.write(0,5,'CPU')
    sheet.write(0,6,'内存')
    sheet.write(0,7,'磁盘')
    sheet.write(0,8,'操作系统')
    sheet.write(0,9,'网卡数')
    sheet.write(0,10,'HBA卡数')
    sheet.write(0,11,'IP地址')
    sheet.write(0,12,'管理地址')
    sheet.write(0,13,'子网掩码')
    sheet.write(0,14,'网关')
    sheet.write(0,15,'机柜号')
    sheet.write(0,16,'机柜位')
    sheet.write(0,17,'HBA卡WWN')
    sheet.write(0,18,'机房')
    sheet.write(0,19,'存储')
    sheet.write(0,20,'剩余存储')
    sheet.write(0,21,'剩余核数')
    sheet.write(0,22,'剩余内存')
    sheet.write(0,23,'所属集群')
    sheet.write(0,24,'所属域')
    sheet.write(0,25,'所属项目')
    sheet.write(0,26,'安装软件')
    sheet.write(0,27,'所属存储组')
    sheet.write(0,28,'所属网络组')
    sheet.write(0,29,'备注')

    row =1
    for i in objs:
        sheet.write(row,0,i.id)
        sheet.write(row,1,i.pmname)
        sheet.write(row,2,i.sn)
        sheet.write(row,3,i.role)
        sheet.write(row,4,i.type)
        sheet.write(row,5,i.cpu)
        sheet.write(row,6,i.memory)
        sheet.write(row,7,i.disk)
        sheet.write(row,8,i.os)
        sheet.write(row,9,i.eth)
        sheet.write(row,10,i.hba)
        sheet.write(row,11,i.ip)
        sheet.write(row,12,i.ilo_ip)
        sheet.write(row,13,i.mask)
        sheet.write(row,14,i.gateway)
        sheet.write(row,15,i.jiguihao)
        sheet.write(row,16,i.jiguiwei)
        sheet.write(row,17,i.hba_wwn)
        sheet.write(row,18,i.position)
        sheet.write(row,19,i.ttstorage)
        sheet.write(row,20,i.systorage)
        sheet.write(row,21,i.sycore)
        sheet.write(row,22,i.symem)
        sheet.write(row,23,i.cluster_id)
        sheet.write(row,24,i.domain_id)
        sheet.write(row,25,i.project_id)
        sheet.write(row,26,i.soft_id)
        sheet.write(row,27,i.storagegroup_id)
        sheet.write(row,28,i.vlangroup_id)
        sheet.write(row,29,i.remark)
        row=row+1
    output = StringIO.StringIO()
    book.save(output)
    output.seek(0)
    response = HttpResponse(output.getvalue(), content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=%s' %fn
    return response


from django.conf.urls import patterns, include, url

urlpatterns = patterns('ProjectManage.views',
    url(r'^project/list/$','project.projectlist',name='projectlist' ),
    url(r'^project/input/$','project.projectinput',name='projectinput' ),
    url(r'^project/query/$','project.projectquery',name='projectquery' ),
    url(r'^project/edit/(?P<ID>\d+)/$', 'project.projectedit', name='projectedit'),
    url(r'^project/delete/(?P<ID>\d+)/$', 'project.projectdelete', name='projectdelete'),
    url(r'^project/showvm/(?P<ID>\d+)/$', 'project.projectshowvm', name='projectshowvm'),
    url(r'^vm/list/$','vm.vmlist',name='vmlist' ),
    url(r'^vm/input/$','vm.vminput',name='vminput' ),
    url(r'^vm/query/$','vm.vmquery',name='vmquery' ),
    url(r'^vm/edit/(?P<ID>\d+)/$', 'vm.vmedit', name='vmedit'),
    url(r'^vm/delete/(?P<ID>\d+)/$', 'vm.vmdelete', name='vmdelete'),
    url(r'^cluster/list/$','cluster.clusterlist',name='clusterlist' ),
    url(r'^cluster/input/$','cluster.clusterinput',name='clusterinput' ),
    url(r'^cluster/query/$','cluster.clusterquery',name='clusterquery' ),
    url(r'^cluster/edit/(?P<ID>\d+)/$', 'cluster.clusteredit', name='clusteredit'),
    url(r'^cluster/delete/(?P<ID>\d+)/$', 'cluster.clusterdelete', name='clusterdelete'),
    url(r'^cluster/showpm/(?P<ID>\d+)/$', 'cluster.clustershowpm', name='clustershowpm'),
    url(r'^pm/list/$','pm.pmlist',name='pmlist' ),
    url(r'^pm/input/$','pm.pminput',name='pminput' ),
    url(r'^pm/query/$','pm.pmquery',name='pmquery' ),
    url(r'^pm/edit/(?P<ID>\d+)/$', 'pm.pmedit', name='pmedit'),
    url(r'^pm/delete/(?P<ID>\d+)/$', 'pm.pmdelete', name='pmdelete'),
)

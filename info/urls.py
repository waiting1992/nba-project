from django.conf.urls import patterns, url

from info import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^player/(?P<player_id>\d+)/$', views.player, name='player'),
		url(r'^coach/(?P<coach_id>\d+)/$', views.coach, name='coach'),
		url(r'^team/(?P<team_id>\d+)/$', views.team, name='team'),
		url(r'^lastteam/(?P<lastteam_id>\d+)/$', views.lastteam, name='lastteam'),
		url(r'^strokeanalysis/(?P<strokeanalysis_id>\d+)/$', views.strokeanalysis, name='strokeanalysis'),
		url(r'css/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root':'/home/supernova/Django/nba/info/templates'}),
		)

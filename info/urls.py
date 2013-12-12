from django.conf.urls import patterns, url

from info import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^(?P<player_id>\d+)/$', views.player, name='player'),
		)

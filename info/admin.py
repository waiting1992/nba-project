#coding:utf-8

from django.contrib import admin
from info.models import Player, Team, Coach, LastTeam

class PlayerAdmin(admin.ModelAdmin):
	fieldsets = [
			('个人信息', {'fields': ['first_name', 'last_name', 'age', 'birthday', 'height', 'weight', 'country', 'city', 'school' ]}),
			('球员信息', {'fields':['ageToNBA', 'timeToNBA','talentShow', 'currentTeam']}),
			]
	list_display = ('first_name', 'last_name', 'city', 'height', 'currentTeam', 'highestScore')
	list_filter = ['currentTeam', 'city']
	search_fields = ['currentTeam', 'first_name', 'last_name']

admin.site.register(Player, PlayerAdmin)

class CoachAdmin(admin.TabularInline):
	model = Coach
	extra = 3

class TeamAdmin(admin.ModelAdmin):
	fieldsets = [
			('基本信息', {'fields':['name']}),
			('地理信息', {'fields':['city', 'boss', 'gymnasium']}),
			('比赛信息', {'fields':['section', 'timeToNBA', 'numOfChampion', 'players']}),
			]
	inlines = [CoachAdmin]

	list_display = ('name', 'city', 'gymnasium', 'section' )

admin.site.register(Team, TeamAdmin)

class LastTeamAdmin(admin.ModelAdmin):
	fieldsets = [
			('', {'fields':['name']}),
			('比赛信息', {'fields':['time', 'team']})
			]
	list_display = ('name', 'team', 'time' )

admin.site.register(LastTeam, LastTeamAdmin)

#coding:utf-8

from django.contrib import admin
from info.models import Player, Team, Coach, LastTeam, StrokeAnalysis

class PlayerAdmin(admin.ModelAdmin):
	fieldsets = [
			('个人信息', {'fields': [
				'first_name', 'last_name', 'suffix',  'age',
				'birthday', 'height', 'weight', 'country', 
				'city', 'school' 
				]}),
			('球员信息', {'fields':[
				'ageToNBA', 'timeToNBA','talentShow', 'currentTeam',
				'number', 'highestScore', 'strokeanalysis'
				]}),
			]
	list_display = ('Player_id', 'first_name', 'last_name', 
			'city', 'height', 'currentTeam', 'highestScore')
	list_filter = ['currentTeam', 'city']
	search_fields = ['currentTeam', 'first_name', 'last_name']

admin.site.register(Player, PlayerAdmin)

class CoachAdmin(admin.ModelAdmin):
	fieldsets = [
			('基本信息', { 'fields':[
				'first_name', 'last_name'
				, 'suffix', 'birthday']}),
			('球队信息', { 'fields':[ 'currentTeam', 'team']}),
			]
	list_display = ( 'Coach_id', 'first_name', 'last_name' )

admin.site.register(Coach, CoachAdmin)

class TeamAdmin(admin.ModelAdmin):
	fieldsets = [
			('基本信息', {'fields':['name']}),
			('地理信息', {'fields':['city', 'boss', 'gymnasium']}),
			('比赛信息', {'fields':['section', 'timeToNBA', 'numOfChampion']}),
			]
	list_display = ('Team_id', 'name', 'city', 'gymnasium', 'section' )

admin.site.register(Team, TeamAdmin)

class LastTeamAdmin(admin.ModelAdmin):
	fieldsets = [
			('赛季信息', {'fields':['team_name', 'season']})
			]
	list_display = ('LA_id','team_name', 'season' )

admin.site.register(LastTeam, LastTeamAdmin)

class StrokeAnalysisAdmin(admin.ModelAdmin):
	fieldsets = [
			('基本信息', {'fields':['season', 'team']}),
			('统计信息', {'fields':['shooting', 'threePS', 
				'penaltyShot', 'offensiveRebounds', 
				'defensiveRebounds','totalRebounds', 'assists',
				'steals', 'blocks', 'mistakes', 'fouls', 'points']}),
			]
	list_display = ('SA_id', 'season', 'team')

admin.site.register(StrokeAnalysis, StrokeAnalysisAdmin)

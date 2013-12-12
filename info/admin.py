#coding:utf-8

from django.contrib import admin
from info.models import Player, Team, Coach

class PlayerAdmin(admin.ModelAdmin):
	fieldsets = [
			('个人信息', {'fields': ['first_name', 'last_name', 'age', 'birthday', 'height', 'weight', 'country', 'city', 'school' ]}),
			('球员信息', {'fields':['ageToNBA', 'timeToNBA','talentShow']}),
			]
	list_display = ('first_name', 'last_name', 'city', 'height', 'currentTeam', 'highestScore')
	list_filter = ['currentTeam', 'city']
	search_fields = ['currentTeam', 'first_name', 'last_name']

admin.site.register(Player, PlayerAdmin)

class CoachAdmin(admin.TabularInline):
	model = Coach
	extra = 3

class TeamAdmin(admin.ModelAdmin):
	fields = ['name','city']
	inlines = [CoachAdmin]

	list_display = ('name', 'city' )

admin.site.register(Team, TeamAdmin)

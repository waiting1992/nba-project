from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("hellow world")

def player(request, player_id):
	return HttpResponse("You're looking at player %s" %player_id)

def team(request, team_id):
	return HttpResponse("You're looking at team %s" %team_id)

def coach(request, coach_id):
	return HttpResponse("You're looking at coach %s" %coach_id)

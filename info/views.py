from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from info.models import Team
# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def player(request, player_id):
	return HttpResponse("You're looking at player %s" %player_id)

def team(request, team_id):
	team = get_object_or_404( Team, pk=team_id)
	return render(request, 'team/team_detail.html', {'team':team})

def coach(request, coach_id):
	return HttpResponse("You're looking at coach %s" %coach_id)

def lastteam(request, lastteam_id):
	return HttpResponse("You're looking at lastteam %s" %lastteam_id)

def strokeanalysis(request, strokeanalysis_id):
	return HttpResponse("You're looking at strokeanalysis %s" %strokeanalysis_id)


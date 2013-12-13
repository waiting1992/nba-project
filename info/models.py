#!/usr/bin/python
# coding: UTF-8
from django.db import models

# Create your models here.

class Team(models.Model):
	Team_id = models.AutoField(primary_key=True,
			verbose_name='球队编号')
	image = models.ImageField(upload_to='team',verbose_name='队徽')
	name = models.CharField(max_length=30,verbose_name='队名')
	city = models.CharField(max_length=30,verbose_name='城市')
	section = models.CharField(max_length=30,verbose_name='分区')
	boss = models.CharField(max_length=30,verbose_name='老板')
	gymnasium = models.CharField(max_length=30,verbose_name='主场')
	timeToNBA = models.CharField(max_length=10,verbose_name='进入NBA')
	numOfChampion = models.IntegerField(verbose_name='总冠军数')

	def __unicode__(self):
		return self.name

class LastTeam(models.Model):
	LA_id = models.AutoField(primary_key=True,
			verbose_name='服役球队编号')
	team_name = models.ForeignKey(Team,verbose_name='球队')
	season = models.CharField(max_length=10,verbose_name='赛季')

	def __unicode__(self):
		return u'%s %s'%(self.team_name,self.season)

class StrokeAnalysis(models.Model):
	SA_id = models.AutoField(primary_key=True,verbose_name='技术统计编号')
#	name = models.CharField(max_length=30,verbose_name='球员')
	season = models.CharField(max_length=10,verbose_name='赛季')
	team = models.ForeignKey(Team,verbose_name='所在球队')
	shooting = models.CharField(max_length=10,verbose_name='投篮')
	threePS = models.CharField(max_length=10,verbose_name='三分')
	penaltyShot = models.CharField(max_length=10,verbose_name='罚球')
	offensiveRebounds = models.FloatField(verbose_name='进攻篮板')
	defensiveRebounds = models.FloatField(verbose_name='防守篮板')
	totalRebounds = models.FloatField(verbose_name='总篮板')
	assists = models.FloatField(verbose_name='助攻')
	steals = models.FloatField(verbose_name='抢断')
	blocks = models.FloatField(verbose_name='盖帽')
	mistakes = models.FloatField(verbose_name='失误')
	fouls = models.FloatField(verbose_name='犯规')
	points = models.FloatField(verbose_name='得分')
	
	def __unicode__(self):
		return u'%d'%(self.SA_id,)


class Player(models.Model):
	Player_id = models.AutoField(primary_key=True, 
			verbose_name='球员编号' )
	image = models.ImageField(upload_to='player',verbose_name='球员相片')
	first_name = models.CharField(max_length=20,verbose_name='名字')
	last_name = models.CharField(max_length=20,verbose_name='姓氏')
	suffix = models.CharField(max_length=10,verbose_name='教名',null=True)
	age = models.IntegerField(verbose_name='年龄')
	birthday = models.DateField(verbose_name='生日')
	height = models.CharField(max_length=10,verbose_name='身高')
	weight = models.CharField(max_length=10,verbose_name='体重')
	country = models.CharField(max_length=30,verbose_name='国家')
	city = models.CharField(max_length=30,verbose_name='城市')
	school = models.CharField(max_length=30,verbose_name='毕业学校')
	ageToNBA = models.CharField(max_length=10,verbose_name='NBA球龄')
	timeToNBA = models.CharField(max_length=10,verbose_name='进入NBA')
	talentShow = models.TextField(verbose_name='选秀情况')
	currentTeam = models.ForeignKey(Team,verbose_name='现役球队')
	lastTeam = models.ManyToManyField(LastTeam,verbose_name='过去所在过的球队')
	number = models.IntegerField(verbose_name='号码')
	highestScore = models.IntegerField(verbose_name='生涯最高分')
	strokeanalysis = models.ManyToManyField(StrokeAnalysis,
			verbose_name='技术统计', null=True, blank=True)

	def __unicode__(self):
		return u'%s %s %s %d'%(self.first_name,self.suffix,self.last_name,self.Player_id)

class Coach(models.Model):
	Coach_id = models.AutoField(primary_key=True,verbose_name='教练编号')
	first_name = models.CharField(max_length=20,verbose_name='名字')
	last_name = models.CharField(max_length=20,verbose_name='姓氏')
	suffix = models.CharField(max_length=10,verbose_name='教名',null=True)
	birthday = models.DateField(verbose_name='生日')
	currentTeam = models.ForeignKey(Team,verbose_name='目前执教球队')
	team = models.ManyToManyField(LastTeam,verbose_name='曾经执教球队',
			null=True, blank=True)

	def __unicode__(self):
		return u'%d %s %s %s' %(self.Coach_id,self.first_name,self.suffix,self.last_name)
	


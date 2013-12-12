#!/usr/bin/python
# coding: UTF-8
from django.db import models

# Create your models here.

class StrokeAnalysis(models.Model):
	name = models.CharField(max_length=30,verbose_name='球员')
	season = models.CharField(max_length=10,verbose_name='赛季')
	team = models.CharField(max_length=15,verbose_name='所在球队')
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
		return u'%s %s'%(self.name,self.season)

class LastTeam(models.Model):
	name = models.CharField(max_length=50,verbose_name='球员或教练')
	time = models.CharField(max_length=10,verbose_name='时间段')
	team = models.CharField(max_length=20,verbose_name='球队')
	
	def __unicode__(self):
		return u'%s %s'%(self.name,self.time)

class Player(models.Model):
	image = models.ImageField(upload_to='player',verbose_name='球员相片', null=True, blank=True)
	first_name = models.CharField(max_length=20,verbose_name='名字')
	last_name = models.CharField(max_length=20,verbose_name='姓氏')
	suffix = models.CharField(max_length=10,verbose_name='教名',null=True, blank=True)
	age = models.IntegerField(verbose_name='年龄', null=True, blank=True)
	birthday = models.DateField(verbose_name='生日', null=True, blank=True)
	height = models.CharField(max_length=10,verbose_name='身高', null=True, blank=True)
	weight = models.CharField(max_length=10,verbose_name='体重', null=True, blank=True)
	country = models.CharField(max_length=30,verbose_name='国家', null=True, blank=True)
	city = models.CharField(max_length=30,verbose_name='城市', null=True, blank=True)
	school = models.CharField(max_length=30,verbose_name='毕业学校', null=True, blank=True)
	ageToNBA = models.CharField(max_length=10,verbose_name='NBA球龄', null=True, blank=True)
	timeToNBA = models.CharField(max_length=10,verbose_name='进入NBA', null=True, blank=True)
	talentShow = models.TextField(verbose_name='选秀情况', null=True, blank=True)
	currentTeam = models.CharField(max_length=20,verbose_name='现役球队', null=True, blank=True)
	lastTeam = models.ManyToManyField(LastTeam,verbose_name='过去所在过的球队', null=True, blank=True)
	number = models.IntegerField(verbose_name='号码', null=True, blank=True)
	highestScore = models.IntegerField(verbose_name='生涯最高分', null=True, blank=True)
	strokeAnalysis = models.ManyToManyField(StrokeAnalysis,verbose_name='技术统计', null=True, blank=True)

	def __unicode__(self):
		return u'%s %s %s'%(self.first_name,self.suffix,self.last_name)
class Team(models.Model):
	image = models.ImageField(upload_to='team',verbose_name='队徽')
	name = models.CharField(max_length=30,verbose_name='姓名')
	city = models.CharField(max_length=30,verbose_name='城市')
	section = models.CharField(max_length=30,verbose_name='分区')
	boss = models.CharField(max_length=30,verbose_name='老板')
	gymnasium = models.CharField(max_length=30,verbose_name='主场')
	timeToNBA = models.CharField(max_length=10,verbose_name='进入NBA')
	numOfChampion = models.IntegerField(verbose_name='总冠军数')
	players = models.ManyToManyField(Player,verbose_name='队员')

	def __unicode__(self):
		return self.name


class Coach(models.Model):
	first_name = models.CharField(max_length=20,verbose_name='名字')
	last_name = models.CharField(max_length=20,verbose_name='姓氏')
	suffix = models.CharField(max_length=10,verbose_name='教名',null=True)
	birthday = models.DateField(verbose_name='生日')
	currentTeam = models.ForeignKey(Team,verbose_name='目前执教球队')
	team = models.ManyToManyField(LastTeam,verbose_name='曾经执教球队')

	def __unicode__(self):
		return u'%s %s %s' %(self.first_name,self.suffix,self.last_name)
	





from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User


class Team(models.Model):
	id = models.AutoField(primary_key=True)
	team = models.CharField(max_length=255)
	member_name = models.CharField(max_length=255)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.team

class Project(models.Model):
	id = models.AutoField(primary_key=True)
	project = models.CharField(max_length=255)
	team_name = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
	status = models.CharField(max_length=50)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.project


class Rank(models.Model):
	id = models.AutoField(primary_key=True)
	rank = models.IntegerField(default=0)
	points = models.IntegerField(default=0)
	project_name = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
	team_name = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
	date = models.DateField(auto_now_add=True)


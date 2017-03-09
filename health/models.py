from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.urls import reverse


# Create your models here.
class HealthFacility(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=200)
	geom = models.PointField(srid=4326)
	district = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	sub_location = models.CharField(max_length=100)
	agency = models.CharField(max_length=100)
	level = models.IntegerField()
	services = models.TextField(blank=True, null=True)
	
	def __unicode__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('centre_detail', args=[self.id])


class MidWife(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	home_location = models.PointField(srid=4326)
	
	def __unicode__(self):
		return self.name


class SupportGroup(models.Model):
	name = models.CharField(max_length=100)
	leader = models.ForeignKey(MidWife)
	meeting_location = models.PointField(srid=4326)
	health_facility = models.ForeignKey(HealthFacility, null=True, blank=True)
	year_formed = models.DateField(null=True, blank=True)
	
	def __unicode__(self):
		return self.name
	
	def get_absolute_url(self):
		reverse('group_detail', args=[self.id])


class FirstVisit(models.Model):
	date = models.DateTimeField(auto_now=True)
	risk_level = models.CharField(max_length=100)
	test_done = models.TextField()
	complete = models.BooleanField(default=False)
	next_visit = models.DateField()
	
	def __unicode__(self):
		if self.complete == True:
			return 'Completed'
		else:
			return "Not Completed"


class SecondVisit(models.Model):
	date = models.DateTimeField(auto_now=True)
	risk_level = models.CharField(max_length=100)
	test_done = models.TextField()
	complete = models.BooleanField(default=False)
	next_visit = models.DateField()
	
	def __unicode__(self):
		return str(self.complete)


class ThirdVisit(models.Model):
	date = models.DateTimeField(auto_now=True)
	risk_level = models.CharField(max_length=100)
	test_done = models.TextField()
	complete = models.BooleanField(default=False)
	next_visit = models.DateField()
	
	def __unicode__(self):
		if self.complete == True:
			return 'Completed'
		else:
			return "Not Completed"


class FourthVisit(models.Model):
	date = models.DateTimeField(auto_now=True)
	risk_level = models.CharField(max_length=100)
	test_done = models.TextField()
	complete = models.BooleanField(default=False)
	next_visit = models.DateField()
	
	def __unicode__(self):
		return str(self.complete)


class Mother(models.Model):
	name = models.CharField(max_length=100)
	id_number = models.CharField(unique=True, max_length=50)
	next_kin = models.CharField(max_length=100, null=True, blank=True)
	home_health_facility = models.ForeignKey(HealthFacility, null=True)
	home_location = models.PointField(srid=4326)
	group = models.ForeignKey(SupportGroup, blank=True, null=True)
	first_visit = models.OneToOneField(FirstVisit, blank=True, null=True)
	second_visit = models.OneToOneField(SecondVisit, blank=True, null=True)
	third_visit = models.OneToOneField(ThirdVisit, blank=True, null=True)
	fourth_visit = models.OneToOneField(FourthVisit, blank=True, null=True)
	
	def __unicode__(self):
		return self.name

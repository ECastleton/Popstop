from __future__ import unicode_literals

from django.db import models

# Create your models here.
    
class Location(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)

class Time(models.Model):
	date = models.DateField()
	locationName = models.CharField(max_length=30)
	startTime = models.CharField(max_length=7)
	endTime = models.CharField(max_length=7)

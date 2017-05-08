from __future__ import unicode_literals

from django.db import models

class EmailList(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    emailAddress = models.CharField(max_length=100)

	 
     
     

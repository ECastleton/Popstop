from django.db import models
from django.utils import timezone

class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return "%s (%s)" % (self.name, self.date)

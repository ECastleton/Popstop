from django.db import models
from django.utils import timezone

class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TimeSlot(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False)
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)

    def __str__(self):
        return "%s at %s-%s" % (self.date, self.start_time, self.end_time)

    def get_location_address(self):
        return location.address
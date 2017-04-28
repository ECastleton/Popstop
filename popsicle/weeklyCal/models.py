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
        return "%s, %s-%s" % (self.date, self.start_time, self.end_time)

    def get_location_address(self):
        return location.address
    
    def is_for_this_week(self):
        """Returns True if a TimeSlot's date was set to a day in the
        current week.
        
        This is done by comparing the year and ISO week numbers of the current
        date and that of a TimeSlot object"""
        current_year, current_week = timezone.now().isocalendar()[:2]
        timeslot_year, timeslot_week = self.date.isocalendar()[:2]
        if (timeslot_year, timeslot_week) == (current_year, current_week):
            return True
        return False

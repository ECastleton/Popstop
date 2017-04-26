from django.shortcuts import render
from .models import TimeSlot

DAYS = (
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
)

def list_events(request, times=TimeSlot.objects.all):
    week_events = {
        'Monday':{},
        'Tuesday':{},
        'Wednesday':{},
        'Thursday':{},
        'Friday':{},
        'Saturday':{},
        'Sunday':{}
    }
    for i in range(7):
        for timeslot in times():
            if timeslot.date.weekday() != i:
                continue

            location = timeslot.location
            week_events[DAYS[i]]["locationName"] = location.name
            week_events[DAYS[i]]["address"] = str(location.address).replace(" ","+")
    return render(request, "weeklyCal/calendar.html", week_events)

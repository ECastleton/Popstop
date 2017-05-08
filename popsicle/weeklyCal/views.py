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
            if not timeslot.is_for_this_week():
                continue

            location = timeslot.location
            week_events[DAYS[i]]["locationName"] = location.name
            week_events[DAYS[i]]["address"] = str(location.address).replace(" ","+")
            week_events[DAYS[i]]["startTime"] = timeslot.start_time
            week_events[DAYS[i]]["endTime"] = timeslot.end_time
    return render(request, "weeklyCal/calendar.html", week_events)


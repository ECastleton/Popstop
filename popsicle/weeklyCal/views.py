from django.shortcuts import render
from .models import Location

def listEvents(events=Location.objects.all):
	weekEvents = {
        'Monday':{},
        'Tuesday':{},
        'Wednesday':{},
        'Thursday':{},
        'Friday':{},
        'Saturday':{},
        'Sunday':{}
    }
	weekDays = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
	for i in range(0,len(weekDays)):
		for event in events():
			if event.date.weekday()==i:
			  #event.location.replace(' ','+')
			  weekEvents[weekDays[i]]["locationName"]=event.locationName
			  weekEvents[weekDays[i]]["address"]="341+Music+Lane,+Grand+Junction+CO"
	return weekEvents

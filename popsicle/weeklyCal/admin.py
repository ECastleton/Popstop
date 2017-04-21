from django.contrib import admin
from .models import *

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ("name", "address")
    ordering = ["name"]

class TimeAdmin(admin.ModelAdmin):
    model = Time
    list_display = ("date", "startTime", "endTime")
    ordering = ["date"]


admin.site.register(Location, LocationAdmin)
admin.site.register(Time, TimeAdmin)


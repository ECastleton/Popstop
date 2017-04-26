from django.contrib import admin
from .models import Location, TimeSlot

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ("name", "address")
    ordering = ["name"]
    search_fields = ["name"]

class TimeSlotAdmin(admin.ModelAdmin):
    model = TimeSlot
    list_display = ("date", "start_time", "end_time", "location")
    ordering = ["date", "start_time"]
    list_filter = ["date"]

admin.site.register(Location, LocationAdmin)
admin.site.register(TimeSlot, TimeSlotAdmin)

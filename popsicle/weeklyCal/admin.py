from django.contrib import admin
from .models import *

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ("name", "address", "date", "start_time", "end_time")
    ordering = ["date"]

admin.site.register(Location, LocationAdmin)

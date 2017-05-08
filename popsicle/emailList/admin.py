from django.contrib import admin
from .models import EmailList

class EmailAdmin(admin.ModelAdmin):
    model = EmailList
    list_display = ("firstName", "lastName", "emailAddress")
    ordering = ["emailAddress"]
    search_fields = ["emailAddress"]
admin.site.register(EmailList, EmailAdmin)

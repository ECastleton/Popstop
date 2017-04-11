from django.contrib import admin
from .models import Flavor, Ingredient, CateringMenu

admin.site.register(CateringMenu)
admin.site.register(Ingredient)
admin.site.register(Flavor)

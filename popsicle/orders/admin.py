from django.contrib import admin
from .models import Flavor, Ingredient, CateringMenu, ProductCategory

class FlavorAdmin(admin.ModelAdmin):
    model = Flavor
    list_display = ("flavor_name", "ingredients_list", "date_added")
    search_fields = ["flavor_name"]
    ordering = ["flavor_name"]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ("ingredient_name", "date_added")
    search_fields = ["ingredient_name"]
    ordering = ["ingredient_name"]

class CateringMenuAdmin(admin.ModelAdmin):
    model = CateringMenu
    list_display = ("menu_name", "start_date", "end_date", "date_created")
    ordering = ["start_date"]

admin.site.register(CateringMenu, CateringMenuAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Flavor, FlavorAdmin)
admin.site.register(ProductCategory)

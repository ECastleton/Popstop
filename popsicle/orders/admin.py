from django.contrib import admin
from .models import Ingredient, Subingredient, Flavor, CateringMenu, ProductCategory

class SubingredientInline(admin.StackedInline):
    model = Subingredient
    extra = 0

class FlavorAdmin(admin.ModelAdmin):
    model = Flavor
    list_display = ("flavor_name", "ingredients_list", "date_added")
    search_fields = ["flavor_name"]
    ordering = ["flavor_name"]
    filter_horizontal = ["ingredients"]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ("ingredient_name", "date_added")
    search_fields = ["ingredient_name"]
    ordering = ["ingredient_name"]
    inlines = [SubingredientInline]

class CateringMenuAdmin(admin.ModelAdmin):
    model = CateringMenu
    list_display = ("menu_name", "start_date", "end_date", "date_created")
    ordering = ["start_date"]

admin.site.register(CateringMenu, CateringMenuAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Flavor, FlavorAdmin)
admin.site.register(ProductCategory)

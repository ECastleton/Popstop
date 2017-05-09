from django.contrib import admin
from django import forms
from .models import Ingredient, Subingredient, Flavor, CateringMenu, ProductCategory

class SubingredientInline(admin.TabularInline):
    model = Subingredient
    extra = 0

class FlavorAdmin(admin.ModelAdmin):
    model = Flavor
    list_display = ("flavor_name", "category", "ingredients_list", "date_added")
    search_fields = ["flavor_name"]
    ordering = ["flavor_name"]
    filter_horizontal = ["ingredients"]
    list_filter = ["category"]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ("ingredient_name", "date_added")
    search_fields = ["ingredient_name"]
    ordering = ["ingredient_name"]
    inlines = [SubingredientInline]

class CateringMenuAdminForm(forms.ModelForm):
    class Meta:
        model = CateringMenu
        fields = ("menu_name", "flavors", "start_date", "end_date")
    
    def clean(self):
        """Validates start and end dates of a menu upon saving."""
        data = self.cleaned_data
        if not data.get("start_date") < data.get("end_date"):
            raise forms.ValidationError("Start date must be earlier than end date")
        return data

class CateringMenuAdmin(admin.ModelAdmin):
    model = CateringMenu
    form = CateringMenuAdminForm
    list_display = ("menu_name", "is_active", "start_date", "end_date", "date_created")
    ordering = ["-start_date"]
    filter_horizontal = ["flavors"]

admin.site.register(CateringMenu, CateringMenuAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Flavor, FlavorAdmin)
admin.site.register(ProductCategory)

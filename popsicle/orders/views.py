import datetime
from django.http import HttpResponse
from django.shortcuts import render

from .models import Flavor, CateringMenu, ProductCategory

flavor_panel_num = 1

def list_ingredients(flavor: Flavor):
    ingredients = []
    queryset = flavor.ingredients.all()
    for i in list(queryset):
        subingredients = i.subingredient_set.all()
        if not subingredients:
            ingredients.append([str(i), None])
        else:
            subs = sorted([str(s) for s in subingredients])
            ingredients.append([str(i), subs])
    return sorted(ingredients)

def list_flavors(flavors: list):
    global flavor_panel_num
    flavor_list = []

    for flavor in flavors:
        ingredients = list_ingredients(flavor)
        flavor_list.append({
            "name": str(flavor),
            "description":str(flavor.description),
            "ingredients": ingredients,
            "collapse_id": flavor_panel_num
        })
        flavor_panel_num += 1
    return flavor_list

def flavor_menu(request):
    global flavor_panel_num
    flavor_panel_num = 1
    accordion_num = 1

    categories = ProductCategory.objects.all()
    category_list = []
    for c in categories:
        category_list.append({
            "name": str(c),
            "flavors": list_flavors(c.get_flavors()),
            "accordion_id": accordion_num
        })
        accordion_num += 1

    context = {"categories": category_list}
    return render(request, "orders/flavors.html", context)

def catering_menu(request):
    global flavor_panel_num
    flavor_panel_num = 1

    cater_lists = CateringMenu.objects.all()
    if not cater_lists:
        return render(request, "orders/catering.html", dict())

    for menu in cater_lists:
        if not menu.is_active():
            continue

        flavors = list_flavors(menu.flavors.all())
        context = {
            "menu_name": str(menu),
            "flavors": flavors
        }
        return render(request, "orders/catering.html", context)
    else:
        return render(request, "orders/catering.html", dict())

def main(request):
    context = dict()
    categories = ProductCategory.objects.all()
    flavor_list = []
    for c in categories:
        flavor_list.append(
            (str(c), list_flavors(c.get_flavors()))
        )
    context = {"flavor_list": flavor_list}

    cater_list = CateringMenu.objects.all()
    if cater_list:
        current_menu = CateringMenu.objects.all()[0]
        flavors = list_flavors(current_menu.flavors.all())
        menu_context = {
            "menu_name": str(current_menu),
            "flavors": flavors
        }
        context["cater_menu"] = menu_context

    return render(request, "orders/main.html", context)

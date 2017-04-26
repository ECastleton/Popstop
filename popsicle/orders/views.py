from django.http import HttpResponse
from django.shortcuts import render
import datetime

from .models import Flavor, CateringMenu, ProductCategory

def list_flavors(flavors: list):
    flavor_list = []
    for flavor in flavors:
        ingredients = [str(i) for i in flavor.ingredients.all()]
        flavor_list.append(
            (str(flavor), sorted(ingredients))
        )
    return sorted(flavor_list)

def flavor_menu(request):
    categories = ProductCategory.objects.all()
    category_list = []
    for c in categories:
        category_list.append(
            (str(c), list_flavors(c.get_flavors()))
        )
    context = {"categories": category_list}
    return render(request, "orders/flavors.html", context)

def catering_menu(request):
    cater_lists = CateringMenu.objects.all()
    if cater_lists:
        current_menu = cater_lists[0]
        flavors = list_flavors(current_menu.flavors.all())
        context = {
            "menu_name": str(current_menu),
            "flavors": flavors
        }
    else:
        context = dict()
    return render(request, "orders/catering.html", context)

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

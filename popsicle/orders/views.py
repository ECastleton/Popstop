from django.http import HttpResponse
from django.shortcuts import render

from .models import Flavor, CateringMenu

def list_flavors(flavors=Flavor.objects.all):
    flavor_list = []
    for flavor in flavors():
        ingredients = [str(i) for i in flavor.ingredients.all()]
        flavor_list.append((str(flavor), ingredients))
    return flavor_list

def flavor_menu(request):
    flavors = list_flavors()
    context = {"flavors": flavors}
    return render(request, "orders/main.html", context)

def catering_menu(request):
    current_menu = CateringMenu.objects.all()[0]
    flavors = list_flavors(current_menu.flavors.all)
    context = {
        "menu_name": str(current_menu),
        "flavors": flavors
    }
    return render(request, "orders/main.html", context)

def main(request):
    context = dict()
    context["flavor_list"] = list_flavors()

    cater_list = CateringMenu.objects.all()
    if cater_list:
        current_menu = CateringMenu.objects.all()[0]
        flavors = list_flavors(current_menu.flavors.all)
        menu_context = {
            "menu_name": str(current_menu),
            "flavors": flavors
        }
        context["cater_menu"] = menu_context

    return render(request, "orders/main.html", context)

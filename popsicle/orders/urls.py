from django.conf.urls import url
from .views import catering_menu, flavor_menu

urlpatterns = [
    url(r"^flavors/", flavor_menu),
    url(r"^catering/", catering_menu)
]

from django.conf.urls import url
from .views import main, catering_menu, flavor_menu

urlpatterns = [
    url(r'^$', main),
    url(r"^flavors/", flavor_menu),
    url(r"^catering/", catering_menu)
]
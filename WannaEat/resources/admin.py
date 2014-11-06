from django.contrib import admin
from establishments.models import Establishment, City
from dishes.models import EstablishmentDishes, Dish

admin.site.register(Establishment)
admin.site.register(City)
admin.site.register(EstablishmentDishes)
admin.site.register(Dish)
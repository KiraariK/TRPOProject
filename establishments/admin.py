from django.contrib import admin
from establishments.models import Establishment, City, EstablishmentBranch, BranchHall, DinnerWagon

admin.site.register(City)
admin.site.register(Establishment)
admin.site.register(EstablishmentBranch)
admin.site.register(BranchHall)
admin.site.register(DinnerWagon)

from django.contrib import admin
from employees.models import Employee
from establishments.models import Establishment, City, EstablishmentBranch, BranchHall, DinnerWagon
from orders.models import Order

admin.site.register(City)
admin.site.register(Establishment)
admin.site.register(EstablishmentBranch)
admin.site.register(BranchHall)
admin.site.register(DinnerWagon)
admin.site.register(Employee)
admin.site.register(Order)

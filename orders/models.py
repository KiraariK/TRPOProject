from django.db import models
from dishes.models import Dish
from establishments.models import EstablishmentBranch, DinnerWagon, Establishment


class Order(models.Model):
    establishment = models.ForeignKey(Establishment, related_name='orders')
    price = models.FloatField(default=0)
    weight = models.IntegerField(default=0)
    client_phone = models.CharField(max_length=10, blank=True, null=True)
    serve_date = models.DateField(blank=True, null=True)
    execution_datetime = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)


class OrderRow(models.Model):
    order = models.ForeignKey(Order, related_name='rows')
    dish = models.ForeignKey(Dish)
    count = models.IntegerField(default=1)


class ServeDinnerWagon(Order):
    table = models.ForeignKey(DinnerWagon)


class Pickup(Order):
    branch = models.ForeignKey(EstablishmentBranch)


class Delivery(Order):
    address = models.CharField(max_length=50)


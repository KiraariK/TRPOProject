from django.db import models
from establishments.models import Establishment, EstablishmentBranch, DinnerWagon
from dishes.models import Dish


class Order(models.Model):
    """"""

    price = models.FloatField()
    weight = models.IntegerField()
    clinet_phone = models.CharField(max_length=10)
    serve_date = models.DateField()
    execution_datetime = models.DateTimeField()
    expire_date = models.DateField()

    #def save(self, force_insert=False, force_update=False, using=None,
    #         update_fields=None):
    #    self.rows.all()
    #    self.expire_date = timezone.now().date() + timedelta(days=5)
    #    super().save(self, force_insert, force_update, using, update_fields)


class OrderRow(models.Model):
    """"""

    order = models.ForeignKey(Order, related_name='rows')
    establishment = models.ForeignKey(Establishment)
    dish = models.ForeignKey(Dish)
    count = models.IntegerField()

    def add():
        count += 1

    def remove():
        count += 1

    def clear():
        count = 0


class ServeDinnerWagon(Order):
    """"""

    table = models.ForeignKey(DinnerWagon)


class Pickup(Order):
    """"""

    branch = models.ForeignKey(EstablishmentBranch)


class Delivery(Order):
    """"""

    address = models.CharField(max_length=50)
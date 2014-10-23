from django.db import models
from dishes.models import EstablishmentDishes

HALL_TYPE = (
    ('0', 'smoking'),
    ('1', 'nonsmoking'),
    )


class Establishment(models.Model):
    """"""

    dish_list = models.ForeignKey(EstablishmentDishes)
    city = models.CharField(max_length=30)
    image_path = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)

    
class EstablishmentBranch(models.Model):
    """"""

    establishment = models.ForeignKey(Establishment)
    address = models.CharField(max_length=50)
    order_phone_number = models.CharField(max_length=10)
    help_phone_number = models.CharField(max_length=10)


class BranchHall(models.Model):
    """"""

    branch = models.ForeignKey(EstablishmentBranch)
    type = models.CharField(max_length=1, choices=HALL_TYPE)
    tables = models.IntegerField()
    served_tables = models.IntegerField()


class DinnerWagon(models.Model):
    """"""

    hall = models.ForeignKey(BranchHall)
    seats = models.IntegerField(default=2)
    is_served = models.BooleanField(default=False)
    serve_to_datetime = models.DateTimeField()
    serve_from_date = models.DateField()

    def serve():
        is_served = True

    def free():
        is_served = False
from django.db import models
from dishes.models import Dish

HALL_TYPE = \
    (
    ('0', 'nothing'),
    ('1', 'smoking'),
    ('2', 'nonsmoking'),
    )


class City(models.Model):
    name = models.CharField(max_length=30, primary_key=True, unique=True)

    def __str__(self):
        return self.name


class Establishment(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True)
    dish_list = models.ManyToManyField(Dish)
    city = models.ForeignKey(City, related_name='establishments')
    # establishment_image = models.ImageField(upload_to='establishments_images')
    description = models.CharField(max_length=300, blank=True, null=True)
    email = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class EstablishmentBranch(models.Model):
    establishment = models.ForeignKey(Establishment, related_name='branches')
    address = models.CharField(max_length=50)
    order_phone_number = models.CharField(max_length=10)
    help_phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.establishment + self.address


class BranchHall(models.Model):
    branch = models.ForeignKey(EstablishmentBranch, related_name='halls')
    type = models.CharField(max_length=1, choices=HALL_TYPE)
    tables_count = models.IntegerField(default=1)
    served_tables_count = models.IntegerField(default=0)

    def __str__(self):
        return self.type


class DinnerWagon(models.Model):
    hall = models.ForeignKey(BranchHall, related_name='dinner_wagons')
    seats = models.IntegerField(default=2)
    is_served = models.BooleanField(default=False)
    serve_to_datetime = models.DateTimeField(blank=True, null=True)
    serve_from_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.hall + self.seats

    def serve(self):
        self.is_served = True

    def free(self):
        self.is_served = False

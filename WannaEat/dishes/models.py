from django.db import models

DISH_TYPE = (
    ('0', 'alcohol'),
    ('1', 'soft_drinks'),
    ('2', 'garnishes'),
    ('3', 'hot_dishes'),
    ('4', 'desserts'),
    ('5', 'snaks'),
    ('6', 'salads'),
    ('7', 'pizzas'),
    ('8', 'rolls'),
    )


class Dish(models.Model):
    """"""

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    composition = models.CharField(max_length=50, blank=True)
    weight = models.IntegerField(blank=True)
    price = models.FloatField()
    category = models.CharField(max_length=1, choices=DISH_TYPE)


class EstablishmentDishes(models.Model):
    """"""

    dish = models.ForeignKey(Dish)
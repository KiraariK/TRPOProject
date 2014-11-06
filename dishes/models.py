from django.db import models

DISH_TYPE = \
    (
    ('0', 'alcohol'),
    ('1', 'soft_drinks'),
    ('2', 'garnishes'),
    ('3', 'hot_dishes'),
    ('4', 'desserts'),
    ('5', 'snakes'),
    ('6', 'salads'),
    ('7', 'pizzas'),
    ('8', 'rolls'),
    )


class Dish(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True, null=True)
    composition = models.CharField(max_length=50, blank=True, null=True)
    # dish_image = models.ImageField(upload_to='dish_images')
    weight = models.IntegerField(blank=True, null=True)
    price = models.FloatField()
    category = models.CharField(max_length=1, choices=DISH_TYPE)

    def __str__(self):
        return self.name
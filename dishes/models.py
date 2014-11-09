from django.db import models
from establishments.models import Establishment

DISH_TYPE = \
    (
    ('0', 'none'),
    ('1', 'alcohol'),
    ('2', 'soft_drinks'),
    ('3', 'garnishes'),
    ('4', 'hot_dishes'),
    ('5', 'desserts'),
    ('6', 'snakes'),
    ('7', 'salads'),
    ('8', 'pizzas'),
    ('9', 'rolls'),
    )


class Dish(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание')
    composition = models.CharField(max_length=50, blank=True, null=True, verbose_name='Состав')
    # dish_image = models.ImageField(upload_to='dishes_images', verbose_name='Картинка')
    weight = models.IntegerField(blank=True, null=True, verbose_name='Вес')
    price = models.FloatField(default=100.0, verbose_name='Цена')
    category = models.CharField(max_length=1, choices=DISH_TYPE, verbose_name='Категория блюда')

    def __str__(self):
        return self.name


class EstablishmentDish(models.Model):
    dish = models.OneToOneField(Dish, related_name='+', verbose_name='Блюдо')
    establishment = models.ForeignKey(Establishment, related_name='dishes', verbose_name='Заведение')

    def __str__(self):
        return '{0}: {1}'.format(
            self.establishment,
            self.dish,
        )
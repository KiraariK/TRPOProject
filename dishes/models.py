from django.db import models
from establishments.models import Establishment


class Dish(models.Model):
    DISH_TYPE_ALCOHOL = '0'
    DISH_TYPE_SOFT_DRINK = '1'
    DISH_TYPE_GARNISH = '2'
    DISH_TYPE_HOT_DISH = '3'
    DISH_TYPE_DESSERT = '4'
    DISH_TYPE_SNAKE = '5'
    DISH_TYPE_SALAD = '6'
    DISH_TYPE_PIZZA = '7'
    DISH_TYPE_ROLL = '8'
    DISH_TYPE_SOUP = '9'

    DISH_TYPE = (
        (DISH_TYPE_ALCOHOL, 'Алкогольные напитки'),
        (DISH_TYPE_SOFT_DRINK, 'Безалкогольные напитки'),
        (DISH_TYPE_GARNISH, 'Гарниры'),
        (DISH_TYPE_HOT_DISH, 'Горячие блюда'),
        (DISH_TYPE_DESSERT, 'Дессерты'),
        (DISH_TYPE_SNAKE, 'Закуски'),
        (DISH_TYPE_SALAD, 'Салаты'),
        (DISH_TYPE_PIZZA, 'Пиццы'),
        (DISH_TYPE_ROLL, 'Роллы'),
        (DISH_TYPE_SOUP, 'Супы'),
    )

    name = models.CharField(
        max_length=30,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    composition = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        verbose_name='Состав'
    )
    dish_image = models.ImageField(
        upload_to='dishes/',
        blank=True,
        null=True,
        verbose_name='Картинка блюда',
    )
    weight = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Вес'
    )
    price = models.FloatField(
        default=100.0,
        verbose_name='Цена'
    )
    category = models.CharField(
        max_length=1,
        choices=DISH_TYPE,
        verbose_name='Категория блюда'
    )

    def __str__(self):
        return self.name


class EstablishmentDish(models.Model):
    dish = models.OneToOneField(
        Dish,
        verbose_name='Блюдо'
    )
    establishment = models.ForeignKey(
        Establishment,
        related_name='dishes',
        verbose_name='Заведение'
    )

    def __str__(self):
        return '{0}: {1}'.format(
            self.establishment,
            self.dish,
        )

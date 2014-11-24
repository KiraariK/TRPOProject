from django.test import TestCase
from dishes.models import Dish, EstablishmentDish
from establishments.models import Establishment, City


class DishTest(TestCase):
    def test_dish_class_name(self):
        dish = Dish(
            name='Гречка',
            price=70.50,
            category=Dish.DISH_TYPE_GARNISH,
        )
        self.assertEqual(dish.__str__(), 'Гречка', "Имя класса неверно")

    def test_dish_name(self):
        dish = Dish(
            name='Борщ',
            price=56.50,
            category=Dish.DISH_TYPE_SOUP,
        )
        self.assertEqual(dish.name, 'Борщ', "Название блюда неверно")

    def test_dish_price(self):
        dish = Dish(
            name='Креветки',
            price=120.5,
            category=Dish.DISH_TYPE_HOT_DISH,
        )
        self.assertEqual(dish.price, 120.5, "Цена блюда неверна")

    def test_dish_category(self):
        dish = Dish(
            name='Мясо Кабана',
            price=230.45,
            category=Dish.DISH_TYPE_HOT_DISH,
        )
        self.assertEqual(dish.category, Dish.DISH_TYPE_HOT_DISH, "Категория блюда неверна")


class EstablishmentDishTest(TestCase):
    def test_establishment_dish_class_name(self):
        dish = Dish(
            name='Паста с курицей',
            price=170.34,
            category=Dish.DISH_TYPE_HOT_DISH,
        )
        city = City(
            name='Tomsk',
        )
        establishment = Establishment(
            name='Пельмени Project',
            city=city,
            email='pelproj@tomsk.ru',
        )

        establishment_dish = EstablishmentDish(
            dish=dish,
            establishment=establishment,
        )
        self.assertEqual(establishment_dish.__str__(), 'Пельмени Project: Паста с курицей',
                         "Имя класса неверно")

    def test_establishment_dish_dish(self):
        dish = Dish(
            name='Борщ',
            price=56.50,
            category=Dish.DISH_TYPE_SOUP,
        )

        establishment_dish = EstablishmentDish(
            dish=dish,
        )
        self.assertIs(establishment_dish.dish, dish, "Неправильное блюдо у заведения")

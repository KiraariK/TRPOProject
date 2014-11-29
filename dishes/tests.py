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

from django.test import TestCase
from establishments.models import City


class CityTest(TestCase):
    def test_city_name(self):
        city = City(name='Tomsk')
        self.assertEqual(city.name, 'Tomsk')

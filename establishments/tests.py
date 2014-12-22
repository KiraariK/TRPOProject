from django.test import TestCase
from establishments.models import City, Establishment, EstablishmentBranch, DinnerWagon, BranchHall

# Todo reserve_table and free_table


class CityTest(TestCase):
    def test_city_name(self):
        city = City(name="Tomsk")
        self.assertEqual(city.name, "Tomsk")


class EstablishmentTest(TestCase):
    def test_establishment_all_fields(self):
        city_test = City(name='Tomsk')
        est = Establishment(name='Vaflia project', city=city_test, email='kakaha@mail.ru')
        self.assertEqual(est.city.__str__(), "Tomsk", "City Name is not equal  with establishment's city name")


class EstablishmentBranchTest(TestCase):
    def test_str(self):
        city_test = City(name='Tomsk')
        est_test = Establishment(name='Vaflia project', city=city_test, email='kakaha@mail.ru')
        estbranch = EstablishmentBranch(establishment=est_test, address="City Tomsk, Vershinina str, 39a",
                                        order_phone_number="99224343", help_phone_number="4324356")
        self.assertEqual(estbranch.__str__(), 'Vaflia project, City Tomsk, Vershinina str, 39a')


class BranchHallTest(TestCase):
    def test_str(self):
        city_test = City(name='Tomsk')
        est_test = Establishment(name='Vaflia project', city=city_test, email='kakaha@mail.ru')
        estbranch = EstablishmentBranch(establishment=est_test, address="City Tomsk, Vershinina str, 39a",
                                        order_phone_number="99224343", help_phone_number="4324356")
        branch_hall = BranchHall(branch=estbranch, type=0)
        self.assertEqual(branch_hall.__str__(), 'Vaflia project, City Tomsk, Vershinina str, 39a - 0')


class DinnerWagonTest(TestCase):
    def test_str(self):
        city_test = City(name='Tomsk')
        est_test = Establishment(name='Vaflia project', city=city_test, email='kakaha@mail.ru')
        estbranch = EstablishmentBranch(establishment=est_test, address="City Tomsk, Vershinina str, 39a",
                                        order_phone_number="99224343", help_phone_number="4324356")
        branch_hall = BranchHall(branch=estbranch, type=0)
        dinner_wagon = DinnerWagon (hall=branch_hall,seats=2)
        self.assertEqual(dinner_wagon.__str__(), 'Vaflia project, City Tomsk, Vershinina str, 39a - 0: 2')
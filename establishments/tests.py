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


class DinnerWagonTest(TestCase):
    def test_dinnerwagon_is_reserved(self):
        city_test = City(name='Tomsk')
        est_test = Establishment(name='Vaflia project', city=city_test, email='kakaha@mail.ru')
        estbranch = EstablishmentBranch(establishment=est_test, address="City Tomsk, Vershinina str, 39a",
                                        order_phone_number="99224343", help_phone_number="4324356")
        esthall = BranchHall(type=1, branch=estbranch, )
        dinerwagon_test = DinnerWagon(hall=esthall, seats=20, is_reserved=False)
        dinerwagon_test.reserve()
        self.assertTrue(dinerwagon_test.is_reserved)

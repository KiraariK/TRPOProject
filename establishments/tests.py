from django.test import TestCase
from establishments.models import City, Establishment, EstablishmentBranch, DinnerWagon, BranchHall


class CityTest(TestCase):
    def test_city_name(self):
        city = City(name="Tomsk")
        self.assertEqual(city.name, "Tomsk")


class EstablishmentTest(TestCase):
    def test_establishment_all_fields(self):
        city_test = City(name='Tomsk')
        est = Establishment(name='Vaflia project', city=city_test,  email='kakaha@mail.ru')
        self.assertEqual(est.name, 'Vaflia project', "Name of establishment is not equal ")
        self.assertEqual(est.city.__str__(), "Tomsk", "City Name is not equal  with establishment's city name")
        if est.description is not None:
            self.assertIn(est.name, est.description, "Name of establishment was not found in description")
        regex_email_str = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        self.assertRegex(est.email, regex_email_str, "Email is not correct")


class EstablishmentBranchTest(TestCase):
    def test_establishmentbranches_all_fields(self):
        city_test = City(name='Tomsk')
        est_test = Establishment(name='Vaflia project', city=city_test,  email='kakaha@mail.ru')
        estbranch = EstablishmentBranch(establishment=est_test, address="City Tomsk, Vershinina str, 39a", order_phone_number="99224343", help_phone_number="4324356")
        self.assertEqual(est_test, estbranch.establishment, "This Establishment hasn't this branch")
        self.assertIn(est_test.city.__str__(), estbranch.address, "City name is not found in adrress of Branch")
        regex_str_only_numbers = r'^([A-Z]*\s?[0-9]*)[\s_-]*([1-9][1-9]*$)?'
        self.assertRegex(estbranch.order_phone_number,regex_str_only_numbers, "Order Tel should include only numbers")
        self.assertRegex(estbranch.help_phone_number,regex_str_only_numbers, "Help Tel should include only numbers")


class DinnerWagonTest(TestCase):
    def test_dinnerwagon_is_reserved(self):
        city_test = City(name='Tomsk')
        est_test = Establishment(name='Vaflia project', city=city_test,  email='kakaha@mail.ru')
        estbranch = EstablishmentBranch(establishment=est_test,address="City Tomsk, Vershinina str, 39a", order_phone_number="99224343", help_phone_number="4324356")
        esthall = BranchHall(type=1, branch=estbranch,)
        dinerwagon_test = DinnerWagon(hall=esthall, seats=20, is_reserved=False)
        dinerwagon_test.reserve()
        self.assertTrue(dinerwagon_test.is_reserved)

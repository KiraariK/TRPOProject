from django.test import TestCase
# TODO accept_order and decline_order
# Create your tests here.
from employees.models import Employee
from establishments.models import Establishment
from orders.models import Order


class EmployeeTest(TestCase):
    def test_employee_str(self):
        est_test = Establishment(name="Vaflia project")
        emp_test = Employee(establishment=est_test)
        self.assertEqual(emp_test.__str__(), 'Аккаунт Vaflia project')

        # def test_acc_order(self):
        # emp_test=Employee()
        # order_test=Order(state=Order.STATE_UNDER_CONSIDERATION)
        #  emp_test.acc_order(order=order_test)
        # self.assertEqual(order_test.state, Order.STATE_IN_PROGRESS)

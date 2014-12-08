from django.views.generic import ListView
from employees.models import Employee
from orders.models import Order


class EmployeePage(ListView):
    model = Employee
    template_name = 'employees/employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees_id = self.kwargs.get('employees_id')
        context['employees'] = Employee.objects.get(id=employees_id)
        return context

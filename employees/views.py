from django.http import HttpResponse
from django.shortcuts import render_to_response
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
        context['order_list'] = Order.objects.filter(contact_account_id=employees_id)

        return context


def acc_state(request):
     if request.is_ajax():
       # order_id = request.GET.get('id')
       # order = Order.objects.get(id=int(order_id))
       # Employee.acc_order(order_id)
        return HttpResponse('1')
     else: return HttpResponse('0')




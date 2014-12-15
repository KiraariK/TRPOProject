from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
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


def login_view(request, login_state):
    # здесь проверить зареган или нет. или хз где
    state = login_state
    if state == '1':
        return render(
            request,
            'employees/authentication.html',
            {
                'title': 'вход',
                'state': 1
            }
        )
    else:
        return render(
            request,
            'employees/authentication.html',
            {
                'title': 'вход',
                'state': 0
            }
        )


def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        employee = Employee.objects.get(user__id=user.id)
        emp_id = employee.id
        if user.is_active:
            auth.login(request, user)
            return redirect('employees', emp_id)
        else:
            return redirect('ban_employee')
    else:

        return redirect('login_employee', 1)


def ban_view(request):
    return render(
        request,
        'employees/ban.html',
        {
            'title': 'Sorry'
        }
    )


def acc_state(request):
    if request.is_ajax():
        # order_id = request.GET.get('id')
        # order = Order.objects.get(id=int(order_id))
        # Employee.acc_order(order_id)
        return HttpResponse('1')
    else:
        return HttpResponse('0')

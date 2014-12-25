import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.views.generic import ListView
from employees.models import Employee
from orders.models import Order, OrdersCartRow


class EmployeePage(ListView):
    model = Employee
    template_name = 'employees/employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees_id = self.kwargs.get('employees_id')
        context['employee'] = Employee.objects.get(id=employees_id)
        employee_orders = Order.objects.filter(contact_account__id=employees_id)
        current_datetime = datetime(
            datetime.now().year,
            datetime.now().month,
            datetime.now().day,
            datetime.now().hour,
            datetime.now().minute
        )
        for order in employee_orders:
            order_execution_datetime = datetime(
                order.execute_date.year,
                order.execute_date.month,
                order.execute_date.day,
                order.execute_time.hour,
                order.execute_time.minute
            )
            if order_execution_datetime <= current_datetime:
                order.perform()
                order.save(update_fields=['state'])
        context['order_list'] = employee_orders.order_by('-execute_date')
        context['employee_user'] = Employee.objects.get(id=employees_id).user

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


def accept_order(request):
    if request.is_ajax():
        order_id = request.GET.get('order_id')
        necessary_order = Order.objects.filter(id=order_id).first()
        if necessary_order.state == Order.STATE_UNDER_CONSIDERATION:
            necessary_order.accept()
            necessary_order.save(update_fields=['state'])
            return HttpResponse(necessary_order.get_state_display())
        else:
            return HttpResponse('cancel')
    else:
        return HttpResponse('error')


def decline_order(request):
    if request.is_ajax():
        order_id = request.GET.get('order_id')
        necessary_order = Order.objects.filter(id=order_id).first()
        if necessary_order.state == Order.STATE_UNDER_CONSIDERATION:
            necessary_order.decline()
            necessary_order.save(update_fields=['state'])
            return HttpResponse(necessary_order.get_state_display())
        else:
            return HttpResponse('cancel')
    else:
        return HttpResponse('error')


def view_order_dish_list(request):
    if request.is_ajax():
        order_id = request.GET.get('id')
        order_rows = OrdersCartRow.objects.filter(order__id=order_id)
        dishes_in_order = {}
        order_price = 0
        for row in order_rows:
            dishes_in_order[row.establishment_dish.dish] = row.dishes_count
            order_price += row.establishment_dish.dish.price * row.dishes_count

        dish_list = []
        for key, val in dishes_in_order.items():
            dish_specification = {'dish_name': key.name, 'dish_price': key.price, 'dish_count': val}
            dish_list.append(dish_specification)
        order_info = {'order_price': order_price, 'order_components': dish_list}

        json_string = json.dumps(order_info, ensure_ascii=False).encode('utf8')
        return HttpResponse(json_string)
    else:
        return HttpResponse('error')

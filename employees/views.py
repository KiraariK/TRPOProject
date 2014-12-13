from django.shortcuts import render, redirect
from django.views.generic import ListView
from employees.models import Employee
from django.contrib import auth


class EmployeePage(ListView):
    model = Employee
    template_name = 'employees/employees.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees_id = self.kwargs.get('employees_id')
        context['employees'] = Employee.objects.get(id=employees_id)
        return context


def login_view(request):
    # здесь проверить зареган или нет. или хз где
    return render(
        request,
        'employees/authentication.html',
        {
            'title': 'вход'
        }
    )


def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            user123 = Employee.objects.filter(user=user)[0]
            auth.login(request, user)
            return redirect('employees', user123.id)
        else:
            return redirect('ban_employee')
    else:
        return redirect('login_employee')


def ban_view(request):
    return render(
        request,
        'employees/ban.html',
        {
            'title': 'Sorry'
        }
    )

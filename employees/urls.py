from django.conf.urls import patterns, url
from employees.views import EmployeePage

urlpatterns = patterns(
    '',
    url(r'(?P<employees_id>\d+)/$', EmployeePage.as_view(), name='employees'),
)

from django.conf.urls import patterns, url
from employees import views
from employees.views import EmployeePage

urlpatterns = patterns(
    '',
    url(r'(?P<employees_id>\d+)/?', EmployeePage.as_view(), name='employees'),

 # url for ajax requests
    url(r'accept_order/$', views.acc_state, name='accept_order')
)

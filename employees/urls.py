from django.conf.urls import patterns, url
from employees import views
from employees.views import EmployeePage

urlpatterns = patterns(
    '',
    url(r'(?P<employees_id>\d+)/$', EmployeePage.as_view(), name='employees'),
    url(r'^accounts/login/(?P<login_state>\d+)?', views.login_view, name='login_employee'),
    url(r'^accounts/ban/$', views.ban_view, name='ban_employee'),
    url(r'^accounts/after_login/$', views.auth_view, name='after_login'),
    # url for ajax requests
    url(r'accept_order/$', views.acc_state, name='accept_order'),
    url(r'^$', views.acc_state, name='decline_order'),
)

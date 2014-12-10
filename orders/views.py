from django.http import HttpResponseNotAllowed, HttpResponse
from django.views.generic import ListView
from django_ajax.decorators import ajax
from orders.models import Order,OrdersCartRow



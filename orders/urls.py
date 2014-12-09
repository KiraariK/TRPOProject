from django.conf.urls import patterns, url
from orders import views

urlpatterns = patterns(
    '',

    url(r'cart/(?P<cart_state>\d+)/$', views.view_cart, name='cart'),

    # url for ajax
    url(r'cart_increment_dish/$', views.increment_dish, name='dish_incrementation'),

    # url for ajax
    url(r'cart_decrement_dish/$', views.decrement_dish, name='dish_decrementation'),
)

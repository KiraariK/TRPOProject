from django.conf.urls import patterns, url
from orders import views

urlpatterns = patterns(
    '',

    url(r'cart/(?P<cart_state>\d+)/$', views.view_cart, name='cart'),

    url(r'cart/orders/$', views.view_orders, name='cart_orders'),

    # url for ajax
    url(r'cart/orders/dish_list$', views.view_establishment_dish_list, name='cart_orders_establishment_dish_list'),

    # url for ajax
    url(r'cart_increment_dish/$', views.increment_dish, name='cart_dish_incrementation'),

    # url for ajax
    url(r'cart_decrement_dish/$', views.decrement_dish, name='cart_dish_decrementation'),
)

from django.conf.urls import patterns, url
from orders import views

urlpatterns = patterns(
    '',

    url(r'cart/(?P<cart_state>\d+)/$', views.view_cart, name='cart'),

    url(r'cart/orders/$', views.view_orders, name='cart_orders'),

    # url for ajax
    url(r'cart/orders/dish_list/$', views.view_establishment_dish_list, name='cart_orders_establishment_dish_list'),

    # url for ajax
    url(r'cart/increment_dish/$', views.increment_dish, name='cart_dish_incrementation'),

    # url for ajax
    url(r'cart/decrement_dish/$', views.decrement_dish, name='cart_dish_decrementation'),

    url(r'make_order/(?P<establishment_id>\d+)/(?P<order_type>\d+)/$', views.get_order_form, name='get_form'),

    url(r'my_orders/$', views.get_user_form, name='get_user_form'),

    # url for ajax
    # url(r'my_orders/dish_list/$', views.view_order_dish_list, name='view_order_dish_list')
)

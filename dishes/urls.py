from django.conf.urls import patterns, url
from dishes import views
from dishes.views import DishesList, DishAbout

urlpatterns = patterns(
    '',

    url(r'(?P<establishment_id>\d+)/$', DishesList.as_view(), name='dishes_without_category'),

    url(r'(?P<establishment_id>\d+)/(?P<dish_category>\d+)?', DishesList.as_view(), name='dishes_with_category'),

    url(r'dish/(?P<dish_id>\d+)/?', DishAbout.as_view(), name='dish_about'),

    # url for ajax requests
    url(r'update_cart/$', views.add_dish, name='cart_updating'),

    # url for ajax requests
    url(r'load_cart/$', views.load_cart, name='cart_loading'),
)

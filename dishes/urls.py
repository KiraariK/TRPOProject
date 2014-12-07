from django.conf.urls import patterns, url
from dishes.views import DishesList

urlpatterns = patterns(
    '',

    url(r'(?P<establishment_id>\d+)/$', DishesList.as_view(), name='dishes'),

    url(r'(?P<establishment_id>\d+)/(?P<dish_category>\d+)?', DishesList.as_view(), name='dishes')
)

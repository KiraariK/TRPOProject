from django.conf.urls import patterns, url
from establishments.views import CityList

urlpatterns = patterns('',
    url(r'^$', CityList.as_view(), name='home'),
)
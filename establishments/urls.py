from django.conf.urls import patterns, url
from establishments.views import EstablishmentsList

urlpatterns = patterns(
    '',

    url(r'^$', EstablishmentsList.as_view(), name='establishments'),

    url(r'(?P<city_id>\d+)/$', EstablishmentsList.as_view(), name='establishments')
)

from django.conf.urls import patterns, url
from establishments import views
from establishments.views import EstablishmentsList

urlpatterns = patterns(
    '',

    url(r'^$', EstablishmentsList.as_view(), name='home'),

    url(r'(?P<city_id>\d+)/$', EstablishmentsList.as_view(), name='establishments'),

    # url for ajax requests
    url(r'flush_session/$', views.delete_expired_session_data, name='session_cleaning'),
)

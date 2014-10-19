from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'OrderSystem.views.home', name='home'),
)
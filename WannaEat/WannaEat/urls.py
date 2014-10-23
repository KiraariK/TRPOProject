"""
Definition of urls for WannaEat.
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', include('OrderSystem.urls', namespace="OrderSystem")),
    #url(r'city/(?P<city_id>\d+)', include('establishments.urls', namespace="establishments")),
    url(r'^$', RedirectView.as_view(url=r'city/')), # redirect to /city/
    url(r'city/', include('establishments.urls', namespace="establishments")),
    #url(r'establishment/(?P<establishment_id>\d+)', include('dishes.urls', namespace="dishes")),
    #url(r'dish/(?P<dish_id>\d+)', include('dishes.urls', namespace="dishes")),
    # TODO do something with the following urls
    #url(r'cart/', include('orders.urls', namespace="orders")),
    #url(r'order/', include('orders.urls', namespace="orders")),
    url(r'admin/', include(admin.site.urls)),
)

#from datetime import datetime
#from django.conf.urls import patterns, url
#from app.forms import BootstrapAuthenticationForm

## Uncomment the next lines to enable the admin:
## from django.conf.urls import include
## from django.contrib import admin
## admin.autodiscover()

#urlpatterns = patterns('',
#    # Examples:
#    url(r'^$', 'app.views.home', name='home'),
#    url(r'^contact$', 'app.views.contact', name='contact'),
#    url(r'^about', 'app.views.about', name='about'),
#    url(r'^login/$',
#        'django.contrib.auth.views.login',
#        {
#            'template_name': 'app/login.html',
#            'authentication_form': BootstrapAuthenticationForm,
#            'extra_context':
#            {
#                'title':'Log in',
#                'year':datetime.now().year,
#            }
#        },
#        name='login'),
#    url(r'^logout$',
#        'django.contrib.auth.views.logout',
#        {
#            'next_page': '/',
#        },
#        name='logout'),

#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#    # Uncomment the next line to enable the admin:
#    # url(r'^admin/', include(admin.site.urls)),
#)

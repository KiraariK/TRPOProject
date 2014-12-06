from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = patterns(
    '',

    # редирект с корня сайта на страницу выбора заведения для города
    url(r'^$', RedirectView.as_view(url=r'city/')),

    # редирект на файл urls в приложении establishments
    url(r'^city/', include('establishments.urls')),

    # редирект на файл urls в приложении establishments
    url(r'^establishment/', include('dishes.urls')),

    # редирект на файл urls в приложении dishes
    # url(r'^dish/', include('dishes.urls', namespace="dishes")),

    # редирект на файл urls в приложении employees
    # url(r'^employee/', include('employees.urls', namespace="employees")),

    # релирект на файл urls в приложении orders
    # url(r'^chart/', include('orders.urls', namespace="orders")),

    # админка сайта
    url(r'^admin/', include(admin.site.urls)),
)

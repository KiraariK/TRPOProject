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

    # url(r'^cart/', include('orders.urls', namespace="orders")),

    # страница пользователя организации
    url(r'^employees/', include('employees.urls')),

    # админка сайта
    url(r'^admin/', include(admin.site.urls)),
)

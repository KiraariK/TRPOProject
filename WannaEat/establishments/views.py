# Create your views here.
from django.http.request import HttpRequest
from django.template.context import RequestContext
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from establishments.models import City, Establishment


#def home(request):
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'establishments/home.html',
#        context_instance = RequestContext(request,
#        {
#            'title':'Home page'
#        })
#    )


class CityList(ListView):
    model = City
    template_name = 'establishments/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        default_city = City.objects.first()
        context['default_city'] = default_city
        context['establishment_list'] = Establishment.objects.filter(city=default_city)
        return context


class CityDetails(DetailView):
    model = City
    template_name = 'establishments/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_list'] = City.objects.all()
        return context

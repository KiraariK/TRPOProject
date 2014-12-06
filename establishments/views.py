from django.views.generic import ListView
from establishments.models import City, Establishment


class EstablishmentsList(ListView):
    model = City
    template_name = 'establishments/establishments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city_id = self.kwargs.get('city_id')
        if city_id is not None:
            default_city = City.objects.filter(id=city_id)[0] or City.objects.first()
        else:
            default_city = City.objects.first()
        context['default_city'] = default_city
        context['establishment_list'] = Establishment.objects.filter(city=default_city)
        return context

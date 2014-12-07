from django.views.generic import ListView, DetailView
from dishes.models import EstablishmentDish, Dish


class DishesList(ListView):
    model = EstablishmentDish
    template_name = 'dishes/dishes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        establishment_id = self.kwargs.get('establishment_id')
        if establishment_id is not None:
            if EstablishmentDish.objects.filter(establishment__id=establishment_id).exists():
                current_establishment = EstablishmentDish.objects.filter(establishment__id=establishment_id)[0]
            else:
                current_establishment = EstablishmentDish.objects.first()
        else:
            current_establishment = EstablishmentDish.objects.first()

        dish_category = self.kwargs.get('dish_category')
        default_dish_category = dish_category or Dish.DISH_TYPE_SOUP
        context['current_establishment'] = current_establishment.establishment
        context['dish_categories_list'] = Dish.DISH_TYPE
        context['default_dish_category'] = default_dish_category
        context['dishes_list'] = Dish.objects.filter(
            establishmentdish__establishment=establishment_id,
            category=default_dish_category,
        )
        context['dish_name'] = EstablishmentDish.return_name
        return context


class DishAbout(ListView):
    model = EstablishmentDish
    template_name = 'dishes/dish_about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish_id = self.kwargs.get('dish_id')
        context['dish'] = Dish.objects.get(id=dish_id)
        return context

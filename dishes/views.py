from django.views.generic import ListView
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
        if dish_category is not None:
            if EstablishmentDish.objects.filter(dish__category=dish_category).exists():
                default_dish_category = dish_category
            else:
                default_dish_category = Dish.DISH_TYPE_SOUP
        else:
            default_dish_category = Dish.DISH_TYPE_SOUP
        context['current_establishment'] = current_establishment.establishment
        # context['dish_categories_list'] = EstablishmentDish.dish.DISH_TYPE
        context['default_dish_category'] = default_dish_category
        # TODO Доделать запись в контекст списка блюд выбранного заведения и выбранной категории + список категорий
        # establishment_dishes = EstablishmentDish.objects.filter(establishment=current_establishment)
        # dish = establishment_dishes.filter(dish__category=default_dish_category)[0]

        # context['dishes_list'] = EstablishmentDish.objects.filter(
        #     establishment=current_establishment,
        #     dish__category=default_dish_category
        # )
        return context

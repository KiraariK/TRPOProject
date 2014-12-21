from django.http import HttpResponse
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
        default_dish_category = dish_category or '100'
        context['current_establishment'] = current_establishment.establishment
        context['dish_categories_list'] = Dish.DISH_TYPE
        context['default_dish_category'] = default_dish_category
        if default_dish_category != '100':
            context['dishes_list'] = Dish.objects.filter(
                establishmentdish__establishment=establishment_id,
                category=default_dish_category,
            )
        else:
            context['dishes_list'] = Dish.objects.filter(
                establishmentdish__establishment=establishment_id
            )
        return context


class DishAbout(ListView):
    model = EstablishmentDish
    template_name = 'dishes/dish_about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish_id = self.kwargs.get('dish_id')
        context['dish'] = Dish.objects.get(id=dish_id)
        return context


def load_cart(request):
    """Загружает сохраненное состояние корзины"""
    if request.is_ajax():
        if request.session.get('cart_price') is not None:
            cart_price = request.session.get('cart_price')
        else:
            cart_price = 0
        message = cart_price
    else:
        message = 'error'
    return HttpResponse(message)


def add_dish(request):
    """Добавляет в сессию блюдо, обновляет значение корзины в сессии"""
    if request.is_ajax():
        dish_id = request.GET.get('id')
        if request.session.get(dish_id) is not None:
            request.session[dish_id] += 1
        else:
            request.session[dish_id] = 1

        dish = Dish.objects.get(id=dish_id)
        if request.session.get('cart_price') is not None:
            request.session['cart_price'] += dish.price
        else:
            request.session['cart_price'] = dish.price

        message = 'ok'
    else:
        message = 'error'
    return HttpResponse(message)

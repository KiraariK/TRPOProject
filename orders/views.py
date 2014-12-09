from django.http import HttpResponse
from django.shortcuts import render
from dishes.models import EstablishmentDish, Dish


def view_cart(request, cart_state):
    """Отображает страницу корзины заказа"""
    # cart_state == '1' - загружаем из сессии параметры корзины
    # cart_state == '0' - очищаем ключи сессии, загружаем пустую корзину
    if cart_state == '0':
        request.session.flush()
        cart_price = 0
        return render(
            request,
            'orders/cart.html',
            {
                'cart_price': cart_price
            }
        )
    else:
        if request.session.get('cart_price') is not None:
            cart_price = request.session.get('cart_price')
        else:
            cart_price = 0

        if cart_price == 0:
            return render(
                request,
                'orders/cart.html',
                {
                    'cart_price': cart_price
                }
            )
        else:
            dishes = {}
            for key in request.session.keys():
                if key != 'cart_price':
                    dishes[EstablishmentDish.objects.get(dish__id=key)] = request.session.get(key)
            cart_dishes = dishes.items()
            return render(
                request,
                'orders/cart.html',
                {
                    'cart_price': cart_price,
                    'cart_dishes': cart_dishes,
                }
            )


def increment_dish(request):
    """Увеличивает количество единиц заданного блюда на 1"""
    if request.is_ajax():
        dish_id = request.GET.get('id')
        dish_price = request.GET.get('price')
        request.session[dish_id] += 1
        request.session['cart_price'] += float(dish_price)
        return HttpResponse(request.session[dish_id])
    else:
        return HttpResponse('error')


def decrement_dish(request):
    """Уменьшает количество единиц заданного блюда на 1"""
    if request.is_ajax():
        dish_id = request.GET.get('id')
        dish_count = request.GET.get('count')
        old_count = request.session.get(dish_id)
        if old_count - int(dish_count) <= 0:
            del request.session[dish_id]
            dec_price = Dish.objects.get(id=dish_id).price * int(dish_count)
            old_cart_price = request.session.get('cart_price')
            if old_cart_price - dec_price <= 0:
                del request.session['cart_price']
            else:
                request.session['cart_price'] -= dec_price
        else:
            request.session[dish_id] -= int(dish_count)
            dec_price = Dish.objects.get(id=dish_id).price * int(dish_count)
            request.session['cart_price'] -= dec_price
        if request.session.get(dish_id) is not None:
            return HttpResponse(request.session[dish_id])
        else:
            return HttpResponse(0)
    else:
        return HttpResponse('error')

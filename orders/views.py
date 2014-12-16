import json
from django.http import HttpResponse
from django.shortcuts import render
from dishes.models import EstablishmentDish, Dish
from orders.models import Order
from orders.forms import TableForm
from orders.forms import DeliveryForm
from orders.forms import PickUpForm


def view_cart(request, cart_state):
    """Отображает страницу корзины заказа"""
    """cart_state == '1' - загружаем из сессии параметры корзины"""
    """cart_state == '0' - очищаем ключи сессии, загружаем пустую корзину"""
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


def view_orders(request):
    """Отображает страницу подготовленных заказов"""
    order_establishments = []
    for key in request.session.keys():
        if key != 'cart_price':
            first_establishment_for_key = EstablishmentDish.objects.filter(dish__id=int(key))[0].establishment
            if order_establishments.count(first_establishment_for_key) == 0:
                order_establishments.append(first_establishment_for_key)

    orders_in_cart = {}
    for establishment in order_establishments:
        establishment_order_price = 0
        for key in request.session.keys():
            if key != 'cart_price':
                if EstablishmentDish.objects.filter(dish__id=int(key))[0].establishment.name == establishment.name:
                    establishment_order_price += \
                        request.session[key] *\
                        EstablishmentDish.objects.get(dish__id=int(key)).dish.price
        orders_in_cart[establishment] = establishment_order_price

    orders = orders_in_cart.items()

    return render(
        request,
        'orders/cart_orders.html',
        {
            'orders': orders
        }
    )


def view_establishment_dish_list(request):
    if request.is_ajax():
        establishment_id = request.GET.get('id')
        establishment = EstablishmentDish.objects.filter(establishment__id=int(establishment_id))[0].establishment
        establishment_dishes_in_order = {}
        for key in request.session.keys():
            if key != 'cart_price':
                if EstablishmentDish.objects.filter(dish__id=int(key))[0].establishment.name == establishment.name:
                    establishment_dishes_in_order[Dish.objects.get(id=int(key))] = request.session[key]

        dish_list = []
        for key, val in establishment_dishes_in_order.items():
            dish_specification = {'dish_name': key.name, 'dish_price': key.price, 'dish_count': val}
            dish_list.append(dish_specification)

        json_string = json.dumps(dish_list, ensure_ascii=False).encode('utf8')
        return HttpResponse(json_string)
    else:
        return HttpResponse('error')


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
        dec_price = Dish.objects.get(id=dish_id).price * int(dish_count)
        if old_count - int(dish_count) <= 0:
            del request.session[dish_id]
            old_cart_price = request.session.get('cart_price')
            if old_cart_price - dec_price <= 0:
                del request.session['cart_price']
            else:
                request.session['cart_price'] -= dec_price
        else:
            request.session[dish_id] -= int(dish_count)
            request.session['cart_price'] -= dec_price
        if request.session.get(dish_id) is not None:
            return HttpResponse(request.session[dish_id])
        else:
            return HttpResponse(0)
    else:
        return HttpResponse('error')


def get_table_form(request):
    order_type = Order.ORDER_TYPE
    # establishment_id = request.GET.get('id')
    # establishment_branch = Order.establishment_branch.objects.filter(establishment__id=int(establishment_id))[0]
    # branch = Order.establishment_branch(request.session['establishment_branch'])
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TableForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TableForm()

    return render(request, 'orders/orders.html', {'form': form, 'order_type': order_type})


def get_delivery_form(request):
    order_type = Order.ORDER_TYPE
    # branch = Order.establishment_branch(request.session['establishment_branch'])
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DeliveryForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DeliveryForm()

    return render(request, 'orders/orders.html', {'form': form, 'order_type': order_type})


def get_pickup_form(request):
    order_type = Order.ORDER_TYPE
    # branch = Order.establishment_branch(request.session['establishment_branch'])
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PickUpForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PickUpForm()

    return render(request, 'orders/orders.html', {'form': form, 'order_type': order_type})


def login(request):
    form = TableForm()
    return render(
        request,
        'orders.html',
        {
            'form': form,
        }
    )


def get_form(request, order_type):
    """Возвращает на страницу соответствующую форму, тип зависит от order_type:
    0 - заказ столика
    1 - заказ самовывоза
    2 - заказ доставки"""
    # проверям, нужно ли вообще пользщователю показывать форму (вдруг он ничего не заказал?)
    if request.session.get('cart_price') is not None:
        order_types = Order.ORDER_TYPE
        if order_type == '0':
            if request.method == 'POST':
                form = TableForm(request.POST)
            else:
                form = TableForm()
            return render(
                request,
                'orders/orders.html',
                {
                    # show_form определяет, нужно ли показывать форму пользователю
                    'show_form': 1,
                    'form': form,
                    'order_types_list': order_types,
                    'current_order_type': order_type
                }
            )
        elif order_type == '1':
            if request.method == 'POST':
                form = PickUpForm(request.POST)
            else:
                form = PickUpForm()
            return render(
                request,
                'orders/orders.html',
                {
                    # show_form определяет, нужно ли показывать форму пользователю
                    'show_form': 1,
                    'form': form,
                    'order_types_list': order_types,
                    'current_order_type': order_type
                }
            )
        elif order_type == '2':
            if request.method == 'POST':
                form = DeliveryForm(request.POST)
            else:
                form = DeliveryForm()
            return render(
                request,
                'orders/orders.html',
                {
                    # show_form определяет, нужно ли показывать форму пользователю
                    'show_form': 1,
                    'form': form,
                    'order_types_list': order_types,
                    'current_order_type': order_type
                }
            )
        else:
            # по-умолчанию - форма для заказа столика
            if request.method == 'POST':
                form = TableForm(request.POST)
            else:
                form = TableForm()
            return render(
                request,
                'orders/orders.html',
                {
                    # show_form определяет, нужно ли показывать форму пользователю
                    'show_form': 1,
                    'form': form,
                    'order_types_list': order_types,
                    'current_order_type': order_type
                }
            )
    else:
        return render(
            request,
            'orders/orders.html',
            {
                # show_form определяет, нужно ли показывать форму пользователю
                'show_form': 0
            }
        )

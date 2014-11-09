from django.db import models
from dishes.models import EstablishmentDish
from establishmentadmins.models import EstablishmentAccount
from establishments.models import EstablishmentBranch, DinnerWagon


ORDER_STATE = \
    (
    ('0', 'none'),
    ('1', 'under_consideration'),
    ('2', 'in_progress'),
    ('3', 'canceled'),
    ('4', 'done'),
    )


ORDER_TYPE = \
    (
    ('0', 'none'),
    ('1', 'dinner_wagon'),
    ('2', 'pickup'),
    ('3', 'delivery'),
    )


class OrdersCart(models.Model):
    weight = models.IntegerField(default=0, verbose_name='Вес')
    price = models.FloatField(default=0.0, verbose_name='Цена')

    def recalculate(self):
        self.weight = 0
        self.price = 0.0
        for row in self.rows.all():
            self.weight += row.establishment_dish.dish.weight * row.dishes_count
            self.price += row.establishment_dish.dish.price * row.dishes_count

    # arguments: row
    def add_row(self, **kwargs):
        if kwargs.get('row') is not None:
            self.rows.append(kwargs.get('row'))
            self.recalculate()

    #arguments: row
    def delete_row(self, **kwargs):
        if kwargs.get('row') is not None:
            for row in self.rows.all():
                if row == kwargs.get('row'):
                    self.rows.remove(kwargs.get('row'))
                    self.recalculate()


class OrdersCartRow(models.Model):
    establishment_dish = models.OneToOneField(EstablishmentDish, related_name='+',
                                              verbose_name='Блюдо заведения')
    dishes_count = models.IntegerField(default=1, verbose_name='Количество блюд')
    orders_cart = models.ForeignKey(OrdersCart, related_name='rows', verbose_name='Корзина заказов')

    def increment(self):
        self.dishes_count += 1
        self.orders_cart.recalculate()

    def decrement(self):
        if self.dishes_count > 1:
            self.dishes_count -= 1
        else:
            self.clean()
        self.orders_cart.recalculate()


class Order(models.Model):
    orders_cart = models.ForeignKey(OrdersCart, related_name='+', verbose_name='Корзина заказов')
    client_phone = models.CharField(max_length=10, verbose_name='Телефон клиента')
    type = models.CharField(max_length=1, choices=ORDER_TYPE, verbose_name='Тип заказа')
    state = models.CharField(max_length=1, choices=ORDER_STATE, verbose_name='Состояние заказа')
    order_date = models.DateField(auto_now_add=True, verbose_name='Дата заказа')
    execute_datetime = models.DateTimeField(verbose_name='Дата исполнения')
    contact_account = models.ForeignKey(EstablishmentAccount, related_name='orders',
                                        verbose_name='Контактное лицо организации')
    # особенные поля, необходимые для определенных видов заказов
    # для заказа столика и самовывоза
    establishment_branch = models.ForeignKey(EstablishmentBranch, blank=True, null=True, related_name='+',
                                             verbose_name='Филиал заведения')
    # для заказа столика
    dinner_wagon = models.ForeignKey(DinnerWagon, blank=True, null=True, related_name='+', verbose_name='Столик')
    # для доставки
    delivery_address = models.CharField(max_length=50, blank=True, null=True, verbose_name='Адрес доставки')

    def acknowledge(self):
        self.state = '2'

    def decline(self):
        self.state = '3'

    def perform(self):
        self.state = '4'
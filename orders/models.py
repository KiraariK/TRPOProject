from datetime import timedelta
from django.db import models
from dishes.models import EstablishmentDish
from employees.models import Employee
from establishments.models import EstablishmentBranch, DinnerWagon


# class OrdersCart(models.Model):
#     weight = models.IntegerField(default=0, verbose_name='Вес')
#     price = models.FloatField(default=0.0, verbose_name='Цена')
#
#     def recalculate(self):
#         self.weight = 0
#         self.price = 0.0
#         for row in self.rows.all():
#             self.weight += row.establishment_dish.dish.weight * row.dishes_count
#             self.price += row.establishment_dish.dish.price * row.dishes_count
#
#     # arguments: row
#     def add_row(self, **kwargs):
#         if kwargs.get('row') is not None:
#             self.rows.append(kwargs.get('row'))
#             self.recalculate()
#
#     #arguments: row
#     def delete_row(self, **kwargs):
#         if kwargs.get('row') is not None:
#             for row in self.rows.all():
#                 if row == kwargs.get('row'):
#                     self.rows.remove(kwargs.get('row'))
#                     self.recalculate()


class Order(models.Model):
    class Meta:
        abstract = True

    STATE_NONE = '0'
    STATE_UNDER_CONSIDERATION = '1'
    STATE_IN_PROGRESS = '2'
    STATE_CANCELED = '3'
    STATE_DONE = '4'

    ORDER_STATE = (
        (STATE_NONE, 'Не установлен'),
        (STATE_UNDER_CONSIDERATION, 'На рассмотрении'),
        (STATE_IN_PROGRESS, 'Выполняется'),
        (STATE_CANCELED, 'Отменен'),
        (STATE_DONE, 'Выполнен'),
    )

    TYPE_DINNER_WAGON = '0'
    TYPE_PICKUP = '1'
    TYPE_DELIVERY = '2'

    ORDER_TYPE = (
        (TYPE_DINNER_WAGON, 'Столик'),
        (TYPE_PICKUP, 'Самовывоз'),
        (TYPE_DELIVERY, 'Доставка'),
    )

    # orders_cart = models.ForeignKey(OrdersCart, related_name='orders', verbose_name='Корзина заказов')
    client_phone = models.CharField(max_length=10, verbose_name='Телефон клиента')
    type = models.CharField(max_length=1, choices=ORDER_TYPE, verbose_name='Тип заказа')
    state = models.CharField(max_length=1, choices=ORDER_STATE, default=STATE_NONE, verbose_name='Состояние заказа')
    order_date = models.DateField(auto_now_add=True, verbose_name='Дата заказа')
    execute_datetime = models.DateTimeField(verbose_name='Дата исполнения')

    @property
    def expire_date(self):
        if self.state == self.STATE_DONE:
            return self.execute_datetime.date() + timedelta(days=30)

    delivery_address = models.CharField(max_length=50, blank=True, null=True, verbose_name='Адрес доставки')
    # contact_account = models.ForeignKey(Employee, related_name='orders',
    #                                     verbose_name='Контактное лицо организации')
    # особенные поля, необходимые для определенных видов заказов

    # для заказа самовывоза
    # establishment_branch = models.ForeignKey(EstablishmentBranch, blank=True, null=True, related_name='+',
    #                                          verbose_name='Филиал заведения')
    # для заказа столика
    # dinner_wagon = models.ForeignKey(DinnerWagon, blank=True, null=True, related_name='orders', verbose_name='Столик')
    # для доставки


class EstablishmentOrder(Order):
    contact_account = models.ForeignKey(Employee, related_name='orders', verbose_name='Заведение')
    dinner_wagon = models.ForeignKey(DinnerWagon, blank=True, null=True, related_name='orders',
                                     verbose_name='Столик')
    establishment_branch = models.ForeignKey(EstablishmentBranch, blank=True, null=True, related_name='+',
                                             verbose_name='Филиал заведения')

    # arguments: type=table or type=pickup or type=delivery
    def make(self, **kwargs):
        if kwargs.get('type') is not None:
            if kwargs.get('type') == 'table':
                self.type = self.TYPE_DINNER_WAGON
                self.dinner_wagon.reserve()
                self.state = self.STATE_UNDER_CONSIDERATION
            if kwargs.get('type') == 'pickup':
                self.type = self.TYPE_PICKUP
                self.state = self.STATE_UNDER_CONSIDERATION
            if kwargs.get('type') == 'delivery':
                self.type = self.TYPE_DELIVERY
                self.state = self.STATE_UNDER_CONSIDERATION

    def accept(self):
        self.state = self.STATE_IN_PROGRESS

    def decline(self):
        if self.type == super().TYPE_DINNER_WAGON:
            self.dinner_wagon.free()
        self.state = self.STATE_CANCELED

    def perform(self):
        if self.type == super().TYPE_DINNER_WAGON:
            self.dinner_wagon.free()
        self.state = self.STATE_DONE


class OrdersCartRow(models.Model):
    establishment_dish = models.OneToOneField(EstablishmentDish, related_name='+', verbose_name='Блюдо заведения')
    dishes_count = models.IntegerField(default=1, verbose_name='Количество блюд')
    order = models.ForeignKey(EstablishmentOrder, related_name='rows', verbose_name='Строка заказа')
    # orders_cart = models.ForeignKey(OrdersCart, related_name='rows', verbose_name='Корзина заказов')

    def increment(self):
        self.dishes_count += 1
        # self.orders_cart.recalculate()

    def decrement(self):
        if self.dishes_count > 1:
            self.dishes_count -= 1
        else:
            self.clean()
        # self.orders_cart.recalculate()

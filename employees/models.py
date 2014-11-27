from django.contrib.auth.models import User
from django.db import models
from establishments.models import Establishment


class Employee(models.Model):
    user = models.ForeignKey(
        User,
        related_name='establishments_accounts',
        verbose_name='Пользователь'
    )
    establishment = models.OneToOneField(
        Establishment,
        related_name='account',
        verbose_name='Заведение'
    )

    def __str__(self):
        return 'Аккаунт {0}'.format(
            self.establishment
        )

    # arguments: order
    def acc_order(self, **kwargs):
        if kwargs.get('order') is not None:
            for order in self.orders.all():
                if order == kwargs.get('order'):
                    order.accept()

    def dec_order(self, **kwargs):
        if kwargs.get('order') is not None:
            for order in self.orders.all():
                if order == kwargs.get('order'):
                    order.decline()

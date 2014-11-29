# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('dishes', '0001_initial'),
        ('establishments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('client_phone', models.CharField(max_length=10, verbose_name='Телефон клиента')),
                ('type', models.CharField(max_length=1, choices=[('0', 'Столик'), ('1', 'Самовывоз'), ('2', 'Доставка')], verbose_name='Тип заказа')),
                ('state', models.CharField(max_length=1, default='0', choices=[('0', 'Не установлен'), ('1', 'На рассмотрении'), ('2', 'Выполняется'), ('3', 'Отменен'), ('4', 'Выполнен')], verbose_name='Состояние заказа')),
                ('order_date', models.DateField(verbose_name='Дата заказа', auto_now_add=True)),
                ('execute_datetime', models.DateTimeField(verbose_name='Дата исполнения')),
                ('delivery_address', models.CharField(max_length=50, blank=True, null=True, verbose_name='Адрес доставки')),
                ('contact_account', models.ForeignKey(related_name='orders', to='employees.Employee', verbose_name='Контактное лицо организации')),
                ('dinner_wagon', models.ForeignKey(related_name='orders', to='establishments.DinnerWagon', verbose_name='Столик', blank=True, null=True)),
                ('establishment_branch', models.ForeignKey(related_name='+', to='establishments.EstablishmentBranch', verbose_name='Филиал заведения', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrdersCartRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('dishes_count', models.IntegerField(verbose_name='Количество блюд', default=1)),
                ('establishment_dish', models.OneToOneField(related_name='+', to='dishes.EstablishmentDish', verbose_name='Блюдо заведения')),
                ('order', models.ForeignKey(related_name='rows', to='orders.Order', verbose_name='Строка заказа')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

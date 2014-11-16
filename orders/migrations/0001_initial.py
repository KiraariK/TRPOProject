# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
        ('employees', '0001_initial'),
        ('establishments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstablishmentOrder',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('client_phone', models.CharField(verbose_name='Телефон клиента', max_length=10)),
                ('type', models.CharField(choices=[('0', 'Столик'), ('1', 'Самовывоз'), ('2', 'Доставка')], verbose_name='Тип заказа', max_length=1)),
                ('state', models.CharField(default='0', choices=[('0', 'Не установлен'), ('1', 'На рассмотрении'), ('2', 'Выполняется'), ('3', 'Отменен'), ('4', 'Выполнен')], verbose_name='Состояние заказа', max_length=1)),
                ('order_date', models.DateField(verbose_name='Дата заказа', auto_now_add=True)),
                ('execute_datetime', models.DateTimeField(verbose_name='Дата исполнения')),
                ('delivery_address', models.CharField(null=True, blank=True, verbose_name='Адрес доставки', max_length=50)),
                ('contact_account', models.ForeignKey(to='employees.Employee', verbose_name='Заведение', related_name='orders')),
                ('dinner_wagon', models.ForeignKey(to='establishments.DinnerWagon', verbose_name='Столик', null=True, related_name='orders', blank=True)),
                ('establishment_branch', models.ForeignKey(to='establishments.EstablishmentBranch', verbose_name='Филиал заведения', null=True, related_name='+', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrdersCartRow',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dishes_count', models.IntegerField(default=1, verbose_name='Количество блюд')),
                ('establishment_dish', models.OneToOneField(to='dishes.EstablishmentDish', verbose_name='Блюдо заведения', related_name='+')),
                ('order', models.ForeignKey(to='orders.EstablishmentOrder', verbose_name='Строка заказа', related_name='rows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

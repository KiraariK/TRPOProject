# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('establishments', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('client_phone', models.CharField(verbose_name='Телефон клиента', max_length=10)),
                ('type', models.CharField(verbose_name='Тип заказа', max_length=1, choices=[('0', 'Столик'), ('1', 'Самовывоз'), ('2', 'Доставка')])),
                ('state', models.CharField(verbose_name='Состояние заказа', max_length=1, default='0', choices=[('0', 'Не установлен'), ('1', 'На рассмотрении'), ('2', 'Выполняется'), ('3', 'Отменен'), ('4', 'Выполнен')])),
                ('order_date', models.DateField(auto_now_add=True, verbose_name='Дата заказа')),
                ('execute_datetime', models.DateTimeField(verbose_name='Дата исполнения')),
                ('delivery_address', models.CharField(null=True, verbose_name='Адрес доставки', blank=True, max_length=50)),
                ('contact_account', models.ForeignKey(verbose_name='Контактное лицо организации', related_name='orders', to='employees.Employee')),
                ('dinner_wagon', models.ForeignKey(to='establishments.DinnerWagon', verbose_name='Столик', related_name='orders', null=True, blank=True)),
                ('establishment_branch', models.ForeignKey(to='establishments.EstablishmentBranch', verbose_name='Филиал заведения', related_name='+', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='establishmentorder',
            name='contact_account',
        ),
        migrations.RemoveField(
            model_name='establishmentorder',
            name='dinner_wagon',
        ),
        migrations.RemoveField(
            model_name='establishmentorder',
            name='establishment_branch',
        ),
        migrations.AlterField(
            model_name='orderscartrow',
            name='order',
            field=models.ForeignKey(verbose_name='Строка заказа', related_name='rows', to='orders.Order'),
        ),
        migrations.DeleteModel(
            name='EstablishmentOrder',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
        ('establishments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('price', models.FloatField()),
                ('weight', models.IntegerField()),
                ('clinet_phone', models.CharField(max_length=10)),
                ('serve_date', models.DateField()),
                ('execution_datetime', models.DateTimeField()),
                ('expire_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('order_ptr', models.OneToOneField(primary_key=True, to='orders.Order', serialize=False, auto_created=True, parent_link=True)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=('orders.order',),
        ),
        migrations.CreateModel(
            name='OrderRow',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('count', models.IntegerField()),
                ('dish', models.ForeignKey(to='dishes.Dish')),
                ('establishment', models.ForeignKey(to='establishments.Establishment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('order_ptr', models.OneToOneField(primary_key=True, to='orders.Order', serialize=False, auto_created=True, parent_link=True)),
                ('branch', models.ForeignKey(to='establishments.EstablishmentBranch')),
            ],
            options={
            },
            bases=('orders.order',),
        ),
        migrations.CreateModel(
            name='ServeDinnerWagon',
            fields=[
                ('order_ptr', models.OneToOneField(primary_key=True, to='orders.Order', serialize=False, auto_created=True, parent_link=True)),
                ('table', models.ForeignKey(to='establishments.DinnerWagon')),
            ],
            options={
            },
            bases=('orders.order',),
        ),
        migrations.AddField(
            model_name='orderrow',
            name='order',
            field=models.ForeignKey(related_name='rows', to='orders.Order'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0001_initial'),
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('price', models.FloatField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('client_phone', models.CharField(null=True, max_length=10, blank=True)),
                ('serve_date', models.DateField(null=True, blank=True)),
                ('execution_datetime', models.DateTimeField(null=True, blank=True)),
                ('expire_date', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('order_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, primary_key=True, to='orders.Order')),
                ('address', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=('orders.order',),
        ),
        migrations.CreateModel(
            name='OrderRow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('count', models.IntegerField(default=1)),
                ('dish', models.ForeignKey(to='dishes.Dish')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('order_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, primary_key=True, to='orders.Order')),
                ('branch', models.ForeignKey(to='establishments.EstablishmentBranch')),
            ],
            options={
            },
            bases=('orders.order',),
        ),
        migrations.CreateModel(
            name='ServeDinnerWagon',
            fields=[
                ('order_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, primary_key=True, to='orders.Order')),
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
        migrations.AddField(
            model_name='order',
            name='establishment',
            field=models.ForeignKey(related_name='orders', to='establishments.Establishment'),
            preserve_default=True,
        ),
    ]

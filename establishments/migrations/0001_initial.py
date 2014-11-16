# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BranchHall',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('type', models.CharField(choices=[('0', 'Курящий'), ('1', 'Не курящий')], verbose_name='Тип зала', max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, verbose_name='Название', unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DinnerWagon',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('seats', models.IntegerField(default=2, verbose_name='Количество мест')),
                ('is_reserved', models.BooleanField(default=False, verbose_name='Занят')),
                ('hall', models.ForeignKey(to='establishments.BranchHall', verbose_name='Зал заведения', null=True, related_name='dinner_wagons', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, verbose_name='Название', unique=True, max_length=50)),
                ('description', models.CharField(null=True, blank=True, verbose_name='Описание', max_length=300)),
                ('email', models.CharField(verbose_name='Электронная почта', unique=True, max_length=30)),
                ('city', models.ForeignKey(to='establishments.City', verbose_name='Город', related_name='establishments')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstablishmentBranch',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('address', models.CharField(verbose_name='Адресс', max_length=50)),
                ('order_phone_number', models.CharField(verbose_name='Телефон заказов', max_length=10)),
                ('help_phone_number', models.CharField(verbose_name='Телефон для справок', max_length=10)),
                ('establishment', models.ForeignKey(to='establishments.Establishment', verbose_name='Заведение', related_name='branches')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='branchhall',
            name='branch',
            field=models.ForeignKey(to='establishments.EstablishmentBranch', verbose_name='Филиал заведения', related_name='halls'),
            preserve_default=True,
        ),
    ]

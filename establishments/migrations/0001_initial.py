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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=1, choices=[('0', 'Курящий'), ('1', 'Не курящий')], verbose_name='Тип зала')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Название')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DinnerWagon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('seats', models.IntegerField(verbose_name='Количество мест', default=2)),
                ('is_reserved', models.BooleanField(verbose_name='Занят', default=False)),
                ('hall', models.ForeignKey(related_name='dinner_wagons', to='establishments.BranchHall', verbose_name='Зал заведения', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('establishment_image', models.ImageField(upload_to='establishments/', blank=True, null=True, verbose_name='Логотип')),
                ('description', models.CharField(max_length=300, blank=True, null=True, verbose_name='Описание')),
                ('email', models.CharField(max_length=30, unique=True, verbose_name='Электронная почта')),
                ('city', models.ForeignKey(related_name='establishments', to='establishments.City', verbose_name='Город')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstablishmentBranch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=80, verbose_name='Адресс')),
                ('order_phone_number', models.CharField(max_length=10, verbose_name='Телефон заказов')),
                ('help_phone_number', models.CharField(max_length=10, verbose_name='Телефон для справок')),
                ('establishment', models.ForeignKey(related_name='branches', to='establishments.Establishment', verbose_name='Заведение')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='branchhall',
            name='branch',
            field=models.ForeignKey(related_name='halls', to='establishments.EstablishmentBranch', verbose_name='Филиал заведения'),
            preserve_default=True,
        ),
    ]

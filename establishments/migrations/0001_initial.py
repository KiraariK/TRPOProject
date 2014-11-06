# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchHall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type', models.CharField(max_length=1, choices=[('0', 'smoking'), ('1', 'nonsmoking')])),
                ('tables_count', models.IntegerField(default=1)),
                ('served_tables_count', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, unique=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DinnerWagon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('seats', models.IntegerField(default=2)),
                ('is_served', models.BooleanField(default=False)),
                ('serve_to_datetime', models.DateTimeField(null=True, blank=True)),
                ('serve_from_date', models.DateField(null=True, blank=True)),
                ('hall', models.ForeignKey(to='establishments.BranchHall', related_name='dinner_wagons')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, unique=True, serialize=False)),
                ('description', models.CharField(null=True, max_length=300, blank=True)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('city', models.ForeignKey(to='establishments.City', related_name='establishments')),
                ('dish_list', models.ManyToManyField(to='dishes.Dish')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstablishmentBranch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('address', models.CharField(max_length=50)),
                ('order_phone_number', models.CharField(max_length=10)),
                ('help_phone_number', models.CharField(max_length=10)),
                ('establishment', models.ForeignKey(to='establishments.Establishment', related_name='branches')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='branchhall',
            name='branch',
            field=models.ForeignKey(to='establishments.EstablishmentBranch', related_name='halls'),
            preserve_default=True,
        ),
    ]

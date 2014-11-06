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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('type', models.CharField(choices=[('0', 'smoking'), ('1', 'nonsmoking')], max_length=1)),
                ('tables', models.IntegerField()),
                ('served_tables', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DinnerWagon',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('seats', models.IntegerField(default=2)),
                ('is_served', models.BooleanField(default=False)),
                ('serve_to_datetime', models.DateTimeField()),
                ('serve_from_date', models.DateField()),
                ('hall', models.ForeignKey(to='establishments.BranchHall')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('image_path', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=20)),
                ('city', models.ForeignKey(to='establishments.City')),
                ('dish_list', models.ForeignKey(to='dishes.EstablishmentDishes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EstablishmentBranch',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('address', models.CharField(max_length=50)),
                ('order_phone_number', models.CharField(max_length=10)),
                ('help_phone_number', models.CharField(max_length=10)),
                ('establishment', models.ForeignKey(to='establishments.Establishment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='branchhall',
            name='branch',
            field=models.ForeignKey(to='establishments.EstablishmentBranch'),
            preserve_default=True,
        ),
    ]

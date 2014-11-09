from django.db import models

HALL_TYPE = \
    (
    ('0', 'none'),
    ('1', 'smoking'),
    ('2', 'nonsmoking'),
    )


class City(models.Model):
    name = models.CharField(max_length=30, primary_key=True, unique=True, verbose_name='Название')

    def __str__(self):
        return self.name


class Establishment(models.Model):
    name = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name='Название')
    city = models.ForeignKey(City, related_name='+', verbose_name='Город')
    # establishment_image = models.ImageField(upload_to='establishments_images', verbose_name='Логотип')
    description = models.CharField(max_length=300, blank=True, null=True, verbose_name='Описание')
    email = models.CharField(max_length=30, unique=True, verbose_name='Электронная почта')

    def __str__(self):
        return self.name


class EstablishmentBranch(models.Model):
    establishment = models.ForeignKey(Establishment, related_name='branches', verbose_name='Заведение')
    address = models.CharField(max_length=50, verbose_name='Адресс')
    order_phone_number = models.CharField(max_length=10, verbose_name='Телефон заказов')
    help_phone_number = models.CharField(max_length=10, verbose_name='Телефон для справок')

    def __str__(self):
        return '{0}, {1}'.format(
            self.establishment,
            self.address,
        )

    # arguments: hall, table, from_date, to_datetime
    def reserve_hall_table(self, **kwargs):
        if kwargs.get('hall') is not None and kwargs.get('table') is not None:
            for hall in self.halls.all():
                if hall == kwargs.get('hall'):
                    hall.reserve_table(table=kwargs.get('table'), from_date=kwargs.get('from_date'),
                                       to_datetime=kwargs.get('to_datetime'))

    # arguments: hall, table
    def free_hall_table(self, **kwargs):
        if kwargs.get('hall') is not None and kwargs.get('table') is not None:
            for hall in self.halls.all():
                if hall == kwargs.get('hall'):
                    hall.free_table(table=kwargs.get('table'))


class BranchHall(models.Model):
    branch = models.ForeignKey(EstablishmentBranch, related_name='halls', verbose_name='Филиал заведения')
    type = models.CharField(max_length=1, choices=HALL_TYPE, verbose_name='Тип зала')
    free_tables_count = models.IntegerField(default=0, verbose_name='Количество свободных столиков')

    def __str__(self):
        return '{0} - {1}'.format(
            self.branch,
            self.type,
        )

    def calculate_free_tables(self):
        self.free_tables_count = 0
        for table in self.dinner_wagons.all():
            if table.is_served == 1:
                self.free_tables_count += 1

    # arguments: table, from_date, to_datetime
    def reserve_table(self, **kwargs):
        if kwargs.get('table') is not None:
            for table in self.dinner_wagons.all():
                if table == kwargs.get('table'):
                    table.reserve(from_date=kwargs.get('from'), to_datetime=kwargs.get('to'))
                    self.calculate_free_tables()

    # arguments: table
    def free_table(self, **kwargs):
        if kwargs.get('table') is not None:
            for table in self.dinner_wagons.all():
                if table == kwargs.get('table'):
                    table.free()
                    self.calculate_free_tables()


class DinnerWagon(models.Model):
    hall = models.ForeignKey(BranchHall, related_name='dinner_wagons', blank=True, null=True,
                             verbose_name='Зал заведения')
    seats = models.IntegerField(default=2, verbose_name='Количество мест')
    is_served = models.BooleanField(default=False, verbose_name='Занят')
    serve_from_date = models.DateField(auto_now_add=True, blank=True, null=True, verbose_name='Когда бронируем')
    serve_to_datetime = models.DateTimeField(blank=True, null=True, verbose_name='На какое время')

    def __str__(self):
        return '{0}: {1}'.format(
            self.hall,
            self.seats,
        )

    # arguments: from_date, to_datetime
    def reserve(self, **kwargs):
        self.is_served = 1
        self.serve_from_date = kwargs.get('from_date')
        self.serve_to_datetime = kwargs.get('to_datetime')

    def free(self):
        self.is_served = 0
        self.serve_from_date = None
        self.serve_to_datetime = None
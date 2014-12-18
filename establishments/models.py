from django.db import models


class City(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name


class Establishment(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название'
    )
    city = models.ForeignKey(
        City,
        related_name='establishments',
        verbose_name='Город'
    )
    establishment_image = models.ImageField(
        upload_to='establishments/',
        blank=True,
        null=True,
        verbose_name='Логотип',
    )
    description = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    email = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Электронная почта'
    )

    def __str__(self):
        return self.name


class EstablishmentBranch(models.Model):
    establishment = models.ForeignKey(
        Establishment,
        related_name='branches',
        verbose_name='Заведение'
    )
    address = models.CharField(
        max_length=80,
        verbose_name='Адресс'
    )
    order_phone_number = models.CharField(
        max_length=10,
        verbose_name='Телефон заказов'
    )
    help_phone_number = models.CharField(
        max_length=10,
        verbose_name='Телефон для справок'
    )

    def __str__(self):
        return '{0}, {1}'.format(
            self.establishment,
            self.address,
        )

    # arguments: hall, table
    def reserve_hall_table(self, **kwargs):
        if kwargs.get('hall') is not None and kwargs.get('table') is not None:
            for hall in self.halls.all():
                if hall == kwargs.get('hall'):
                    hall.reserve_table(table=kwargs.get('table'))

    # arguments: hall, table
    def free_hall_table(self, **kwargs):
        if kwargs.get('hall') is not None and kwargs.get('table') is not None:
            for hall in self.halls.all():
                if hall == kwargs.get('hall'):
                    hall.free_table(table=kwargs.get('table'))


class BranchHall(models.Model):
    HALL_TYPE_SMOKING = '0'
    HALL_TYPE_NONSMOKING = '1'

    HALL_TYPE = (
        (HALL_TYPE_SMOKING, 'Курящий'),
        (HALL_TYPE_NONSMOKING, 'Не курящий'),
    )

    branch = models.ForeignKey(
        EstablishmentBranch, related_name='halls',
        verbose_name='Филиал заведения'
    )
    type = models.CharField(
        max_length=1,
        choices=HALL_TYPE,
        verbose_name='Тип зала'
    )

    @property
    def free_tables_count(self):
        return self.dinner_wagons.filter(
            is_served=1
        ).len()

    def __str__(self):
        return '{0} - {1}'.format(
            self.branch,
            self.get_type_display(),
        )

    # arguments: table
    def reserve_table(self, **kwargs):
        if kwargs.get('table') is not None:
            for table in self.dinner_wagons.all():
                if table == kwargs.get('table'):
                    table.reserve()

    # arguments: table
    def free_table(self, **kwargs):
        if kwargs.get('table') is not None:
            for table in self.dinner_wagons.all():
                if table == kwargs.get('table'):
                    table.free()


class DinnerWagon(models.Model):
    hall = models.ForeignKey(
        BranchHall,
        related_name='dinner_wagons',
        blank=True,
        null=True,
        verbose_name='Зал заведения'
    )
    seats = models.IntegerField(
        default=2,
        verbose_name='Количество мест'
    )
    is_reserved = models.BooleanField(
        default=False,
        verbose_name='Занят'
    )

    def __str__(self):
        return '{0}: {1}'.format(
            self.hall,
            self.seats,
        )

    def reserve(self):
        self.is_reserved = 1
        # self.save()

    def free(self):
        self.is_reserved = 0
        # self.save()

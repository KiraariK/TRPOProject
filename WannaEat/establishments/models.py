#from django.db import models
#from django.utils import timezone
#from _datetime import timedelta


#DISH_TYPE = (
#    ('0', 'alcohol'),
#    ('1', 'soft_drinks'),
#    ('2', 'garnishes'),
#    ('3', 'hot_dishes'),
#    ('4', 'desserts'),
#    ('5', 'snaks'),
#    ('6', 'salads'),
#    ('7', 'pizzas'),
#    ('8', 'rolls'),
#    )


#HALL_TYPE = (
#    ('0', 'smoking')
#    ('1', 'nonsmoking')
#    )


#class Establishment(models.Model):
#    """"""

#    dish_list = models.ForeignKey(EstablishmentDishes)
#    city = models.CharField(max_length=30)
#    image_path = models.CharField(max_length=50)
#    name = models.CharField(max_length=50)
#    email = models.CharField(max_length=20)

    
#class EstablishmentBranch(models.Model):
#    """"""

#    establishment = models.ForeignKey(Establishment)
#    address = models.CharField(max_length=50)
#    order_phone_number = models.CharField(max_length=10)
#    help_phone_number = models.CharField(max_length=10)


#class BranchHall(models.Model):
#    """"""

#    branch = models.ForeignKey(EstablishmentBranch)
#    type = models.CharField(max_lenght=1, choices=HALL_TYPE)
#    tables = models.IntegerField()
#    served_tables = models.IntegerField()


#class DinnerWagon(models.Model):
#    """"""

#    hall = models.ForeignKey(BranchHall)
#    seats = models.IntegerField(default=2)
#    is_served = models.BooleanField(default=false)
#    serve_to_datetime = models.DateTimeField()
#    serve_from_date = models.DateField()

#    def serve():
#        is_served = true

#    def free():
#        is_served = false


#class Dish(models.Model):
#    """"""

#    name = models.CharField(max_length=20)
#    description = models.CharField(max_length=100, blank=true)
#    composition = models.CharField(max_length=50, blank=true)
#    weight = models.IntegerField(blank=true)
#    price = models.FloatField()
#    category = models.CharField(max_length=1, choices=DISH_TYPE)


#class EstablishmentDishes(models.Model):
#    """"""

#    dish = models.ForeignKey(Dish)


#class OrderRow(models.Model):
#    """"""

#    order = models.ForeignKey(Order, related_name='rows')
#    dish = models.ForeignKey(Dish)
#    count = models.IntegerField()

#    def add():
#        count += 1

#    def remove():
#        count += 1

#    def clear():
#        count = 0


#class Order(models.Model):
#    """"""

#    price = models.FloatField()
#    weight = models.IntegerField()
#    clinet_phone = models.CharField(max_length=10)
#    serve_date = models.DateField()
#    execution_datetime = models.DateTimeField()
#    expire_date = models.DateField()

#    def save(self, force_insert=False, force_update=False, using=None,
#             update_fields=None):
#        self.rows.all()
#        self.expire_date = timezone.now().date() + timedelta(days=5)
#        super().save(self, force_insert, force_update, using, update_fields)


#class ServeDinnerWagon(Order):
#    """"""

#    table = models.ForeignKey(DinnerWagon)


#class Pickup(Order):
#    """"""

#    branch = models.ForeignKey(EstablishmentBranch)


#class Delivery(Order):
#    """"""

#    address = models.CharField(max_length=50)
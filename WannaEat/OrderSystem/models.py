# �������� ��� ������������� ����������� __init__
# ����� �� ��� "����" ������������ � ��� ��������� �� ������ 1:M

#from django.db import models


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


#class City(models.Model):
#    """�����, � ������� ����� ���������� ���������"""

#    name = models.CharField(max_length=30)


#class Establishment(models.Model):
#    """��������� ������: ����, �������� � �.�."""

#    city = models.ForeignKey(City)
#    dish_list = models.ForeignKey(EstablishmentDishes)
#    name = models.CharField(max_length=50)
#    email = models.CharField(max_length=20)

    
#class EstablishmentBranch(models.Model):
#    """������ ���������"""

#    establishment = models.ForeignKey(Establishment)
#    address = models.CharField(max_length=50)
#    order_phone_number = models.CharField(max_length=10)
#    help_phone_number = models.CharField(max_length=10)


#class BranchHall(models.Model):
#    """��� � ������� ���������"""

#    branch = models.ForeignKey(EstablishmentBranch)
#    type = models.CharField(max_lenght=1, choices=HALL_TYPE)


#class DinnerWagon(models.Model):
#    """������ � ���� ������� ���������"""

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
#    """����� ��� ������ � ����������"""

#    name = models.CharField(max_length=20)
#    description = models.CharField(max_length=100, blank=true)
#    composition = models.CharField(max_length=50, blank=true)
#    weight = models.IntegerField(blank=true)
#    price = models.FloatField()
#    category = models.CharField(max_length=1, choices=DISH_TYPE)


## �������� ��� ��, ��� ������������ ������ ���� � ���������
#class EstablishmentDishes(models.Model):
#    """������ ���� ����������� ���������"""

#    dish = models.ForeignKey(Dish)


#class OrderRow(models.Model):
#    """������ ������"""

#    dish = models.ForeignKey(Dish)
#    count = models.IntegerField()

#    def add():
#        count += 1

#    def remove():
#        count += 1

#    def clear():
#        count = 0


#class Order(models.Model):
#    """����� � ���������"""

#    order_rows = models.ForeignKey(OrderRow)
#    price = models.FloatField()
#    weight = models.IntegerField()
#    clinet_phone = models.CharField(max_length=10)
#    serve_date = models.DateField()
#    execution_datetime = models.DateTimeField()
#    expire_date = models.DateField()


#class ServeDinnerWagon(Order):
#    """����� ������� � ���������"""

#    table = models.ForeignKey(DinnerWagon)


#class Pickup(Order):
#    """����� ����������"""

#    branch = models.ForeignKey(EstablishmentBranch)


#class Delivery(Order):
#    """����� ��������"""

#    address = models.CharField(max_length=50)
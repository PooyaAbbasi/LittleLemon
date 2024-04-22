from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Booking(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000, blank=True)
    last_modification_time = models.DateTimeField(auto_now=True)
    # purchases = models.ManyToManyField('Menu', related_name='purchases', blank=True)

    def __str__(self):
        return f'guest name:{self.first_name} {self.last_name} \n' + \
                f' guest number:{self.guest_number} -- last update time:{self.last_modification_time}'


class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(null=True)
    menu_item_description = models.TextField(max_length=1000, default='', blank=True)

    def __str__(self):
        return f'{self.name}'

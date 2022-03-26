from django.db import models

from django.conf import settings
from sympy import product
from users.models import User

from django.contrib import auth
import datetime

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.

class Order(models.Model):

    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    resquest_date = models.DateField(default=datetime.date.today)
    product = models.TextField()
    quantity = models.IntegerField()

    class Meta:
        db_table = 'order'

    def __str__(self):
        return str(self.quantity) + " " + self.product + " ordered by " + self.owner.username
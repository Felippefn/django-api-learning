from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    pass

class Person(models.Model):
    class Meta:
        permissions = [("can_eat_pizzas", "Can eat pizzas")]


class Student(Person):
    class Meta:
        proxy = True
        permissions = [("can_deliver_pizzas", "Can deliver pizzas")]

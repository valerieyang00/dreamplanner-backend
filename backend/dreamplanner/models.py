from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Destination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='destinations')
    name = models.CharField(max_length=100)
    budget = models.FloatField()
    photo = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Expense(models.Model):
    date = models.DateField(auto_now=False)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='expenses')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='expenses')
    class Category(models.TextChoices):
        Transportation = 'transportation'
        Lodging = 'lodging'
        Food = 'food'
        Activities = 'activities'
        Miscellaneous = 'misc'
    category = models.CharField(max_length=50, choices=Category.choices)
    merchant = models.CharField(max_length=100)
    amount = models.FloatField()
    details = models.CharField(max_length=250)

    def __str__(self):
        return self.amount

# Create your models here.

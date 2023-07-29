from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    appetizer = models.CharField(max_length=100)
    main_course = models.CharField(max_length=100)
    dessert = models.CharField(max_length=100)
    votes_count = models.PositiveIntegerField(default=0)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

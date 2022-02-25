from django.db import models

# Create your models here.


class Person(models.Model):
  first_name = models.CharField(max_length=64)
  origination = models.CharField(max_length=64)
  destination_city = models.CharField(max_length=64)
  destination_state = models.CharField(max_length=2)
  date = models.DateField()
  time = models.TimeField()
  age = models.IntegerField(default=0)
  pets = models.BooleanField(default=False)
  seats_available = models.IntegerField(default=0)

from django.db import models

# Create your models here.
class Car(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    citizen = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_make_year = models.IntegerField()
    price = models.FloatField()
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)

